import sys
from time import sleep
import math
print("Witaj w kalkulatorze użytkowniku!")


def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    return a / b


def potegowanie(a, b):
    return a ** b


def pierwiastkowanie(a):
    return math.sqrt(a)


def procenty(a, b):
    return a * b * 0.01


def odwrotnosc_liczby(a):
    return 1 / a


def wartosc_bezwzgledna(a):
    return abs(a)


if __name__ == "__main__":
    while True:
        sleep(0.5)
        print("\n1-dodawanie\n2-odejmowanie\n3-mnozenie\n4-dzielenie\n5-potęga\n6-pierwiastek\n7-procenty\n8-odwrotność liczby\n9-wartość bezwzględna\n10-wyjdź")
        try:
            dzialanie = int(input("Wybierz działanie: "))
        except ValueError:
            print("Wpisz odpowiednią liczbę aby wybrać działanie!")
            sleep(0.5)
            continue
        if dzialanie == 1:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
                second_num = int(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            print("Wynik tego działania to:", dodawanie(first_num, second_num))
            sleep(1)
        elif dzialanie == 2:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
                second_num = int(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            print("Wynik tego działania to:", odejmowanie(first_num, second_num))
            sleep(1)
        elif dzialanie == 3:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
                second_num = int(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            print("Wynik tego działania to:", mnozenie(first_num, second_num))
            sleep(1)
        elif dzialanie == 4:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
                second_num = int(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            try:
                print("Wynik tego działania to:", dzielenie(first_num, second_num))
            except ZeroDivisionError:
                print("Nie wolno dzielić przez zero!")
                continue
            sleep(1)
        elif dzialanie == 5:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
                second_num = int(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            print("Wynik tego działania to:", potegowanie(first_num, second_num))
            sleep(1)
        elif dzialanie == 6:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            print("Wynik tego działania to:", pierwiastkowanie(first_num))
            sleep(1)
        elif dzialanie == 7:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
                second_num = int(input("Podaj drugą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            print("Wynik tego działania to:", procenty(first_num, second_num))
            sleep(1)
        elif dzialanie == 8:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            try:
                print("Wynik tego działania to:", odwrotnosc_liczby(first_num))
            except ZeroDivisionError:
                print("Nie wolno dzielić przez zero!")
                continue
            sleep(1)
        elif dzialanie == 9:
            try:
                first_num = int(input("Podaj pierwszą liczbę: "))
            except ValueError:
                print("Wpisz liczbę!")
                continue
            print("Wynik tego działania to:", wartosc_bezwzgledna(first_num))
            sleep(1)
        elif dzialanie == 10:
            sys.exit("Do zobaczenia!")
        else:
            print("Wybrano liczbę z niewłaściwego zakresu!")
