import pyautogui as gui
import time

def AltTabLoop(tabs, count, refresh, refresh_count):
    gui.keyDown('alt')
    i=0
    while i < count:
        time.sleep(.05)
        gui.press('tab')
        time.sleep(.05)
        i += 1
    gui.keyUp('alt')
    if count == (tabs-1):
        count=1
    else:
        count=count+1
    if refresh >= 20:
        time.sleep(1)
        gui.hotkey('ctrl', 'r')
        if refresh_count == 2:
            refresh == 0
            refresh_count = 0
        refresh_count += 1
    return tabs, count, refresh, refresh_count