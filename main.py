import pyautogui
import asyncio

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

async def move_to(x, y, duration=0):
    await asyncio.get_event_loop().run_in_executor(None, lambda: pyautogui.moveTo(x, y, duration=duration))

async def click():
    await asyncio.get_event_loop().run_in_executor(None, pyautogui.click)

async def right_click():
    await asyncio.get_event_loop().run_in_executor(None, pyautogui.rightClick)

async def double_click():
    await asyncio.get_event_loop().run_in_executor(None, pyautogui.doubleClick)

async def press(key):
    await asyncio.get_event_loop().run_in_executor(None, lambda: pyautogui.press(key))

async def write(text, interval=0):
    await asyncio.get_event_loop().run_in_executor(None, lambda: pyautogui.write(text, interval=interval))

async def hotkey(*keys):
    0

    await asyncio.get_event_loop().run_in_executor(None, lambda: pyautogui.hotkey(*keys))

async def drag_to(x, y, duration=0.5):
    await asyncio.get_event_loop().run_in_executor(None, lambda: pyautogui.dragTo(x, y, duration=duration))

async def move(x, y, duration=0):
    await asyncio.get_event_loop().run_in_executor(None, lambda: pyautogui.move(x, y, duration=duration))

async def sleep(seconds):
    await asyncio.sleep(seconds)

async def main():


    # Firefox
    await move_to(937, 1051, duration=0)
    await right_click()
    await move(0, -120, duration=0)
    await click()
    await sleep(1)
    
    # Открываем Twitch
    await move_to(899, 653, duration=0)
    await double_click()
    await sleep(0.5)
    await press('enter')
    await sleep(0.5)
    
    # Поиск канала
    await move_to(1920/2, 1080/2, duration=0)
    await move(-100, -430, duration=0)
    await click()
    await write('At0m', interval=0)
    await press('enter')
    await move(-310, 150, duration=0)
    await click()

    await sleep(1)
    # Создание записи
    await move_to(241, 137, duration=0)
    await hotkey('win', 'shift', 'r')
    await click()
    await drag_to(1578, 885, duration=1)
    await move_to(853, 33, duration=0)
    await sleep(0.5)
    await click()
    await sleep(0.5)
    await click()
    
    # Запись
    await sleep(60)
    
    # Завершение записи
    await move_to(889, 33, duration=0)
    await click()
    await sleep(0.5)
    await move_to(1412, 108, duration=0)
    await click()
    await sleep(0.5)
    await move_to(333, 342, duration=0)
    await click()
    await move_to(1015, 577, duration=0)
    await click()
    

if __name__ == "__main__":
    asyncio.run(main())