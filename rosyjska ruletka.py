import sys
import time
from random import randrange
survived = 0
print("Witaj w grze rosyjska ruletka!")
while True:
    try:
        naboj = int(input("Wybierz jeden nabój od 1 do 6: "))
    except ValueError:
        print("Wpisz liczbę!")
        naboj = 1
        continue
    strzal = randrange(1, 7)
    if naboj <= 0 or naboj > 6:
        print("Wpisałeś złą liczbę!")
        continue

    if strzal == naboj:
        print("Naciągasz kurek...")
        time.sleep(1)
        print("BANG")
        time.sleep(0.5)
        sys.exit("Zginąłeś!")
    else:
        print("Naciągasz kurek...")
        time.sleep(1)
        print("BANG")
        time.sleep(0.5)
        print("Przeżyłeś!")
        survived += 1
    if survived == 5:
        print("Brawo przeżyłeś 5 razy!")
