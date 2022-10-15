import pyautogui, time, keyboard, webbrowser

def documentogoogle(texto):
    webbrowser.open("https://docs.google.com/document/u/0/?tgif=d")
    time.sleep(2)
    pyautogui.moveTo(326, 356, duration=1)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.leftClick()
    keyboard.write(texto)

def youtube(texto):
    webbrowser.open("https://www.youtube.com/")
    time.sleep(3)
    pyautogui.moveTo(566, 122, duration=0.3)
    pyautogui.leftClick()
    keyboard.write(texto)
    keyboard.press_and_release("enter")
    time.sleep(1)
    pyautogui.moveTo(610, 350, duration=0.3)
    pyautogui.leftClick()