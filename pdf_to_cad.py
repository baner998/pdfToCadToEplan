import pyautogui as gui, time

# def identifyloc():
#     while True:
#         currentMouseX, currentMouseY = gui.position()
#         print(currentMouseX,currentMouseY)
#         time.sleep(3)
# identifyloc()

gui.moveTo(1000, 380)
gui.click()
gui.press('escape')
# time.sleep(1)

# pix = gui.pixel(1000, 380)
#
# print(pix)

for page_nr in range(2, 85):

    time.sleep(0.5)
    gui.typewrite('import', interval=0.05)
    gui.press('enter')

    while gui.pixel(1000, 380)[0] != 255:
        time.sleep(0.1)
    gui.typewrite(str(page_nr) + '_BB3.pdf', interval=0.05)
    gui.press('enter')

    while gui.pixel(1000, 380)[0] != 240:
        time.sleep(0.1)
    gui.press('enter')

    while gui.pixel(1000, 380)[0] > 50:
        time.sleep(0.1)
    gui.typewrite('save', interval=0.05)
    gui.press('enter')

    while gui.pixel(1000, 380)[0] != 240:
        time.sleep(0.1)
    gui.typewrite(str(page_nr) + '_BB3', interval=0.05)
    time.sleep(0.05)
    gui.press('enter')

    while gui.pixel(1000, 380)[0] > 50:
        time.sleep(0.1)
    gui.keyDown('ctrl')
    gui.press('a')
    gui.keyUp('ctrl')
    time.sleep(0.2)
    gui.press('delete')


