import altTab
import time
import signal
import os

def SigIntHandler(signum, frame):
    global toggle
    print("You inputted signal number: ", signum, " Which was called in frame: ", frame)
    if(toggle):
        print("\nNo longer looping through tabs, press ctrl + C to resume.\n")
    else:
        print("\nNow looping through tabs, press ctrl + C to pause.\n")
        print("To keep vscode out of the loop, alt tab all tabs until vscode is the last tab in the menu.\n")
    print("To stop the program completely type:\nkill ", os.getpid(), "\nin the command prompt.")
    if(toggle):
        toggle=False
    else:
        toggle=True
    
def main():
    signal.signal(signal.SIGINT, SigIntHandler)
    global toggle
    toggle=True
    tabs=4
    count=1
    refresh=0
    refresh_count = 0
    while(True):
        if(toggle):
            tabs, count, refresh, refresh_count = altTab.AltTabLoop(tabs, count, refresh, refresh_count)
            print("Press ctrl + C to pause the program and see how to end this program")
            refresh += 1
            time.sleep(30)

main()