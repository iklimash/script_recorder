import asyncio
import io
import os
import subprocess
import sys
from datetime import datetime

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CHANNEL_NAME = "gmhikaru"
CHECK_INTERVAL = 60  
OUTPUT_DIR = "recordings"  #


if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_stream_status():

    try:
        url = f"https://www.twitch.tv/{CHANNEL_NAME}"
        response = requests.get(url, timeout=10)
        return "isLiveBroadcast" in response.text
    except:
        return False

def start_recording():

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{OUTPUT_DIR}/{CHANNEL_NAME}_{timestamp}.mp4"

    command = [
        "streamlink",
        f"https://www.twitch.tv/{CHANNEL_NAME}",
        "best",  # Записываем в лучшем качестве
        "-o", filename,
        "--retry-streams", "30",  # Повторять попытки подключения
        "--retry-open", "10"      # Количество попыток открыть поток
    ]

    print(f"Начинаю запись трансляции в файл: {filename}")
    process = subprocess.Popen(command)
    return process, filename

async def monitor_and_record():

    recording_process = None
    current_filename = None

    print(f"Начинаю мониторинг канала {CHANNEL_NAME}...")

    while True:
        try:
            is_live = get_stream_status()

            if is_live and recording_process is None:

                recording_process, current_filename = start_recording()
                print("Трансляция началась, начинаю запись...")

            elif not is_live and recording_process is not None:

                print("Трансляция закончилась, останавливаю запись...")
                recording_process.terminate()
                recording_process.wait()
                recording_process = None
                print(f"Запись сохранена как: {current_filename}")


            await asyncio.sleep(CHECK_INTERVAL)

        except Exception as e:
            print(f"Ошибка: {e}")
            await asyncio.sleep(CHECK_INTERVAL)


def run_as_service():

    if os.name == 'nt':

        batch_content = f"""
        @echo off
        :loop
        python {os.path.basename(__file__)}
        timeout /t 60
        goto loop
        """

        with open("run_as_service.bat", "w") as f:
            f.write(batch_content)

        print("Создан файл run_as_service.bat. Запустите его для работы в фоновом режиме.")


if __name__ == "__main__":

    asyncio.run(monitor_and_record())

    run_as_service()
