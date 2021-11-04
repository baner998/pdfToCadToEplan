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

page_list = ['005', '006', '007', '008', '009', '010', '011', '012', '013', '021', '022',
             '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037',
             '038', '039', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052A', '052B',
             '052C', '052D', '052E', '052F', '052G', '052H', '053A', '053B', '053C', '053D', '061', '063', '065', '069',
             '070', '072', '072A', '073', '074', '075', '080', '081', '083', '084', '085', '088', '089', '090', '091',
             '104', '105', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119',
             '121', '122', '123', '130', '131', '132', '133', '134', '135', '136', '138', '139', '140', '141', '142',
             '143', '191', '192', '193', '195', '196', '197', '198', '201', '202', '203', '204', '205', '206', '211',
             '221', '222', '231', '232']

sheet_list = page_list

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
    while gui.pixel(1019, 556)[0] != 240:
        time.sleep(0.1)
        temp_count = temp_count + 1

        if temp_count > 10:
            gui.keyDown('ctrl')
            gui.keyDown('shift')
            gui.press('i')
            gui.keyUp('ctrl')
            gui.keyUp('shift')

        # wpisuje nazwe pliku
    gui.typewrite(page_nr + '_BB1.dwg', interval=0.05)
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
    gui.typewrite(sheet_nr, interval=0.05)

    # zatwierdzam numer
    gui.press('enter')
    time.sleep(0.1)

    # zatwierdzam wstawienie strony
    gui.press('enter')
