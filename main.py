import pyautogui
from time import sleep

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


# Size(width=1920, height=1080).
# Point(x=0, y=0)
print(pyautogui.position())


pyautogui.moveTo(937, 1051, duration=0) 
pyautogui.rightClick()
pyautogui.move(0, -120, duration=0) 
pyautogui.click()
sleep(1)
pyautogui.moveTo(899, 653, duration=0)# открываю twitch
pyautogui.doubleClick()
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.moveTo(1920/2, 1080/2, duration=0)
pyautogui.move(-100, -430, duration=0)
pyautogui.click()
pyautogui.write('starkycast', interval=0)
pyautogui.press('enter')
pyautogui.move(-310, 150, duration=0)
pyautogui.click()
pyautogui.moveTo(241, 137, duration=0)
pyautogui.hotkey('win', 'shift', 'r')
pyautogui.dragTo(1578, 885, duration=0.5)
pyautogui.moveTo(853, 33, duration=0)
sleep(0.5)
pyautogui.click()
sleep(0.5)
pyautogui.click()
sleep(5) # скок по времени записывать
pyautogui.moveTo(889, 33, duration=0)
pyautogui.click()
sleep(0.5)
pyautogui.moveTo(1412, 108, duration=0)
pyautogui.click()
sleep(0.5)
pyautogui.moveTo(333, 342, duration=0)
pyautogui.click()
pyautogui.moveTo(1015, 577, duration=0)
pyautogui.click()