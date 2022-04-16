import random
import time
wins = 0
odpowiedzi = ('Papier', 'Kamień', 'Nożyce')
print("Witaj w grze papier kamień nożyce!")
while True:
    if wins == 5:
        print("Gratulacje wygrałeś 5 razy!")
    try:
        print("\nJeśli chcesz skończyć grę wpisz 0 jeśli nie:")
        user_answer = int(input("Wybierz mądrze\n1-papier\n2-kamień\n3-nożyce\n----> "))
    except ValueError:
        print("Wpisz liczbę od 1 do 3 aby wybrać znak!")
        continue
    else:
        pass
    computer_answer = random.sample(odpowiedzi, 1)
    time.sleep(0.3)
    if user_answer == 0:
        print("Dziękuję za grę!")
        print(f"Udało ci się wygrać {wins} razy!")
        break
    elif user_answer == 1:
        print("Wybrałeś papier!")
        time.sleep(0.25)
        print("komputer wybrał", computer_answer[0])
        if computer_answer[0] == odpowiedzi[0]:
            print("\nRemis!")
            time.sleep(1)
        elif computer_answer[0] == odpowiedzi[1]:
            print("\nGratulacje, wygrałeś!")
            time.sleep(1)
            wins += 1
        else:
            print("\nNiestety, przegrałeś!")
            time.sleep(1)
    elif user_answer == 2:
        print("komputer wybrał", computer_answer[0])
        time.sleep(0.25)
        print("Wybrałeś kamień!")
        if computer_answer[0] == odpowiedzi[0]:
            print("\nNiestety, przegrałeś!")
            time.sleep(1)
        elif computer_answer[0] == odpowiedzi[1]:
            print("\nRemis!")
            time.sleep(1)
        else:
            print("\nGratulacje, wygrałeś!")
            time.sleep(1)
            wins += 1
    elif user_answer == 3:
        print("komputer wybrał", computer_answer[0])
        time.sleep(0.25)
        print("Wybrałeś nożyce!")
        if computer_answer[0] == odpowiedzi[0]:
            print("\nGratulacje, wygrałeś!")
            time.sleep(1)
            wins += 1
        elif computer_answer[0] == odpowiedzi[1]:
            print("\nNiestety, przegrałeś!")
            time.sleep(1)
        else:
            print("\nRemis!")
            time.sleep(1)
    else:
        print("Wybrano niewłaściwą liczbę!")
