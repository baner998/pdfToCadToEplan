import pyautogui as gui, time


def identifyloc():
    while True:
        currentMouseX, currentMouseY = gui.position()
        print("pos:")
        print(currentMouseX,currentMouseY)
        pix = gui.pixel(currentMouseX, currentMouseY)
        print("colour:")
        print(pix)
        print("-------------")
        time.sleep(1)

identifyloc()
