print("Witaj w programie do obliczania średniej szkolnej!")
#witamy użytkownika odpowiednim komunikatem
def srednia():
    return suma_ocen / ilosc_ocen
#definiujemy funkcje średnia
while True:
    #zamykamy program w pętli while True - pętli nieskończonej
    print("Wpisz ocenę\nJeśli nie ma już więcej ocen wpisz wartość 0")
    suma_ocen = 0
    ilosc_ocen = 0
    #musimy przypisać wartość zmiennej by ją zdefiniować
    while True:
        #kiedy użytkownik nie zakończył podawania ocen:
        try:
            ocena = int(input("Podaj ocenę: "))
        except ValueError:
            print("WPISZ LICZBĘ!")
            break
            ocena = 0
        if ocena >= 7 or ocena < 0:
            print("Wpisz ocenę od 1 do 6!")
            #jeśli użytkownik wybrał złą ocenę wtedy kończymy działanie programu
            break
        elif ocena != 0:
            #sprawdzamy czy użytkownik zakończył działanie programu
            suma_ocen += ocena
            ilosc_ocen += 1
        else:
            #jeśli nie wyświetlamy wartość średniej
            print("ZAKOŃCZONO!")
            print("średnia to:", srednia())
