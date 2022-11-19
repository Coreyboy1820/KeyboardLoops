import pyautogui as gui
import time

def AltTabLoop(tabs, count):
    gui.keyDown('alt')
    i=0
    while i < count:
        time.sleep(.05)
        gui.press('tab')
        time.sleep(.05)
        i = i + 1
    gui.keyUp('alt')
    if count == (tabs-1):
        count=1
    else:
        count=count+1
    time.sleep(1)
    gui.hotkey('ctrl', 'r')
    return tabs, count