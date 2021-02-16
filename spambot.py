import pyautogui, time

time.sleep(5)
f = open("spamtext", 'r')
text = f.readlines()
for _ in range(25):
    for word in text:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
