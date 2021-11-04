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

page_list = ['02', '03', '04', '05', '06', '07', '08', '09', '010', '011', '012', '013', '021', '022', '023',
             '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038',
             '039', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052A', '052B', '052C',
             '052D', '052E', '052F', '052G', '052H', '053A', '053B', '053C', '053D', '061', '063', '065', '069', '070',
             '072', '072A', '073', '074', '075', '080', '081', '083', '084', '085', '088', '089', '090', '091', '104',
             '105', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '121',
             '122', '123', '130', '131', '132', '133', '134', '135', '136', '138', '139', '140', '141', '142', '143',
             '191', '192', '193', '195', '196', '197', '198', '201', '202', '203', '204', '205', '206', '211', '221',
             '222', '231', '232']

for page_nr in page_list:

    # 01 - "open"
    time.sleep(0.5)
    gui.typewrite('open', interval=0.05)
    time.sleep(0.5)
    gui.press('enter')

    # 02 - poczekać na pole wprowadzania tekstu
    while gui.pixel(752, 574)[0] != 255:
        time.sleep(0.1)

    # 03 - wpisać nazwę
    gui.typewrite('UCP-' + page_nr, interval=0.05)
    time.sleep(0.2)

    # 04 - zatwierdzić wpisaną nazwę pliku do otworzenia
    gui.press('enter')

    # 05 poczekać, aż plik się załaduje
    time.sleep(1.0)

    # 06 - "save"
    gui.typewrite('save', interval=0.05)
    time.sleep(0.2)

    # 07 - poczekać na menu zapisu
    while gui.pixel(752, 574)[0] != 255:
        time.sleep(0.1)
    time.sleep(0.3)
    # 08 - zaznaczyć folder, w ktorym ma być zapisany plik
    gui.moveTo(420, 198)
    time.sleep(0.1)
    gui.click()
    gui.press('enter')
    time.sleep(0.1)

    # 09 - pojedyncze klikniecie w polu nazwy
    gui.moveTo(752, 574)
    time.sleep(0.1)
    gui.click()
    time.sleep(0.1)

    # 10 - wpisanie nazwy do zapisu pliku
    gui.typewrite(page_nr + '_BB1', interval=0.05)
    time.sleep(0.1)

    # 11 - kliknięcie w liste rozszerzen
    gui.moveTo(635, 600)
    time.sleep(0.1)
    gui.click()


    # 12 - wybor rozszerzenia z 2010
    gui.moveTo(700, 415)
    while gui.pixel(700, 415)[2] != 215:
        time.sleep(0.1)
    gui.click()
    time.sleep(0.2)

    # 13 - klikniecie zapisz
    gui.moveTo(914, 575)
    gui.click()
    time.sleep(0.2)

    # 14 - close
    gui.typewrite('close', interval=0.05)
    time.sleep(0.1)
    gui.press('enter')
    time.sleep(0.4)
