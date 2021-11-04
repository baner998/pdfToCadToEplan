import pyautogui as gui, time

# def identifyloc():
#     while True:
#         currentMouseX, currentMouseY = gui.position()
#         print(currentMouseX,currentMouseY)
#         pix = gui.pixel(currentMouseX, currentMouseY)
#         print(pix)
#         time.sleep(1)
#
# identifyloc()

time.sleep(3)
# gui.moveTo(1000, 380)
# gui.click()
# gui.press('escape')

page_list = [21, 23, 25, 26, 27, 31, 37, 62, 63, 64, 65, 72, 73, 74, 76, 77, 78, 80, 83, 84, 85]

sheet_list = [32, 34, 36, 37, 38, 44, 61, 127, 128, 131, 132, 183, 184, 185, 196, 197, 198, 200, 213, 221, 222]

for page_nr, sheet_nr in zip(page_list, sheet_list):
    time.sleep(0.8)
    # zaimportowanie
    gui.keyDown('ctrl')
    gui.keyDown('shift')
    gui.press('i')
    gui.keyUp('ctrl')
    gui.keyUp('shift')

    # czekam aż pojawi się okno, a jeśli długo się nie pojawi to raz jeszcze skrót klawiszowy
    temp_count = 0
    while gui.pixel(624, 645)[0] != 240:
        time.sleep(0.1)
        temp_count = temp_count + 1

        if temp_count > 10:
            gui.keyDown('ctrl')
            gui.keyDown('shift')
            gui.press('i')
            gui.keyUp('ctrl')
            gui.keyUp('shift')

        # wpisuje nazwe pliku
    gui.typewrite('bb3_' + str(page_nr) + '.dwg', interval=0.05)
    gui.press('enter')

    # czekam, aż pojawi się okno ze źródłem i schematem
    while gui.pixel(1275, 273)[0] != 240:
        time.sleep(0.1)
    gui.press('enter')

    # czekam na okno z wpisaniem numeru strony schematu
    while gui.pixel(581, 228)[0] != 240:
        time.sleep(0.1)

    # przesuwam się o tyle miejsc, ile trzeba
    while gui.pixel(1192, 282)[0] != 0:
        gui.press('right')
        time.sleep(0.1)



    # # przesuwam się o 3 miejsca
    # time.sleep(0.1)
    # gui.press('right')
    # # czekam, aż program przeskoczy do pola '='
    # while gui.pixel(950, 285)[0] != 0:
    #     time.sleep(0.1)
    # gui.press('right')
    #
    # # czekam, aż program przeskoczy do pola '+'
    # while gui.pixel(1071, 285)[0] != 0:
    #     time.sleep(0.1)
    # gui.press('right')
    #
    # # czekam, aż program przeskoczy do komórki z numerem strony
    # while gui.pixel(1192, 282)[0] != 0:
    #     time.sleep(0.1)

    # podaje numer strony
    gui.typewrite(str(sheet_nr), interval=0.05)

    # zatwierdzam numer
    gui.press('enter')
    time.sleep(0.1)

    # zatwierdzam wstawienie strony
    gui.press('enter')
