import pyautogui as gui, time

def identifyloc():
    gui.moveTo(1000, 380)
    while True:
        currentMouseX, currentMouseY = gui.position()
        pix = gui.pixel(currentMouseX, currentMouseY)
        print(currentMouseX, currentMouseY, pix)

        #gui.moveTo(1000, 380)
        time.sleep(4)
# identifyloc()

time.sleep(3)
#gui.moveTo(1000, 380)
gui.click()
gui.press('escape')
# time.sleep(1)

# pix = gui.pixel(1000, 380)
#
# print(pix)

time.sleep(3)

#  initPath = 'D:\199_PROJEKTY_Inne\CADtoDWG\gravotech_cd_0711\singlePages\'


for page_nr in range(2, 5):

    time.sleep(0.5)
    gui.typewrite('import', interval=0.05)
    gui.press('enter')

    #  wait for DIALOG BOX
    while gui.pixel(850, 380)[0] != 255:
        time.sleep(0.1)
    gui.typewrite(str(page_nr) + '_page.pdf', interval=0.05)
    gui.press('enter')

    #  wait for "import" menu
    while gui.pixel(850, 380)[0] != 128:
        time.sleep(0.1)
    gui.press('enter')

    while gui.pixel(1000, 380)[0] > 50:
        time.sleep(0.1)
    gui.typewrite('save', interval=0.05)
    gui.press('enter')

    while gui.pixel(1300, 650)[0] != 240:
        time.sleep(0.1)
    gui.typewrite(str(page_nr) + '_page', interval=0.05)
    time.sleep(0.05)
    gui.press('enter')

    while gui.pixel(850, 380)[0] > 50:
        time.sleep(0.1)
    gui.keyDown('ctrl')
    gui.press('a')
    gui.keyUp('ctrl')
    time.sleep(0.2)
    gui.press('delete')


