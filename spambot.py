# Modules needed for the bot
import pyautogui, time
# Time before the script starts to run
time.sleep(5)
# Open the .txt file with which you wish to spam someone
f = open(#"NameOfThe.TxtFile", 'r')
# Read all lines of the .txt file and store in text variable
text = f.readlines()
# for loop with determined number of times each line should be spammed
for _ in range(#enter number of times each line should be spammed as an int):
    # for each word in text, spam 
    for word in text:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
