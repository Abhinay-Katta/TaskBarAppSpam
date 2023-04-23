import pyautogui as pag

try:
    with pag.hold('win'):
        while (True):
            for i in range(0, 10):
                pag.press(str(i))
except:
    exit()
