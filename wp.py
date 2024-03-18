import pyautogui
import time
time.sleep(5)
count = 0
while count <= 100:
    pyautogui.typewrite("SASI"+str(count))
    pyautogui.press("enter")
    count += 1
