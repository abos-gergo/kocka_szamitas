import math
import time
import os

def clear_console():
    os.system('cls')

def draw_line():
    print('----------------------------------------------------------')

def kocka_felszin():
    print('Kocka felszínszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Térfogat')
    print('2. Oldal hossza')
    print('3. Lapátló hossza')
    print('4. Testátló hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()
    if opcio == 1:
        terfogat : float = 0
        while terfogat <= 0:
            terfogat : float = float(input('Adja meg a kocka térfogatát! (cm3)'))
            if terfogat <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = terfogat ** (1/3) #Köbgyök
        felszin : float = 6 * oldal * oldal
        print(f'A kocka felszíne: {felszin} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        oldal : float = 0
        while oldal <= 0:
            oldal : float = float(input('Adja meg az oldal hosszát! (cm)'))
            if oldal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        felszin : float = 6 * oldal * oldal
        print(f'A kocka felszíne: {felszin} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 3:
        diagonal : float = 0
        while diagonal <= 0:
            diagonal : float = float(input('Adja meg a lapátló hosszát! (cm)'))
            if diagonal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = math.sqrt((diagonal ** 2) / 2)
        felszin : float = 6 * oldal * oldal
        print(f'A kocka felszíne: {felszin} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 4:
        diagonal : float = 0
        while diagonal <= 0:
            diagonal : float = float(input('Adja meg a testátló hosszát! (cm)'))
            if diagonal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = diagonal / math.sqrt(3)
        felszin : float = 6 * oldal * oldal
        print(f'A kocka felszíne: {felszin} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def kocka_terfogat():
    print('Kocka térfogatszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Felszín')
    print('2. Oldal hossza')
    print('3. Lapátló hossza')
    print('4. Testátló hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()

    if opcio == 1:
        felszin : float = 0
        while felszin <= 0:
            felszin : float = float(input('Adja meg a kocka felszínét! (cm2)'))
            if felszin <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = math.sqrt(felszin / 6)
        terfogat : float = oldal ** 3
        print(f'A kocka térfogata: {terfogat} köbcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        oldal : float = 0
        while oldal <= 0:
            oldal : float = float(input('Adja meg az oldal hosszát! (cm)'))
            if oldal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        terfogat : float = oldal ** 3
        print(f'A kocka térfogata: {terfogat} köbcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 3:
        diagonal : float = 0
        while diagonal <= 0:
            diagonal : float = float(input('Adja meg a lapátló hosszát! (cm)'))
            if diagonal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = math.sqrt((diagonal ** 2) / 2)
        terfogat : float = oldal ** 3
        print(f'A kocka térfogata: {terfogat} köbcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 4:
        diagonal : float = 0
        while diagonal <= 0:
            diagonal : float = float(input('Adja meg a testátló hosszát! (cm)'))
            if diagonal <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        oldal : float = diagonal / math.sqrt(3)
        terfogat : float = oldal ** 3
        print(f'A kocka térfogata: {terfogat} köbcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def main():
    print("Program a kocka felszínének és térfogatának kiszámolására.")
    draw_line()
    while True:
        print('Mit szeretne tenni?')
        print('1. Felszín kiszámolása')
        print('2. Térfogat kiszámolása')
        print('3. Kilépés a programból')
        opcio : int = int(input('Adja meg az opció számát: '))
        draw_line()
        if opcio == 1:
            kocka_felszin()
        elif opcio == 2:
            kocka_terfogat()
        elif opcio == 3:
            print('Kilépés a programból...')
            quit()

if __name__ == "__main__":
    main()