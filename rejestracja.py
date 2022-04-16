import random
import smtplib
registration = True
log = True
status = 2
weryfikacja = int(input("Czy chcesz wprowadzić weryfikację 2-etapową? 1-tak 2-nie\n-----> "))
while status == 2:
    while registration:
        print("Proszę się zarejestrować")
        login = input("Podaj login: ")
        password = input("Podaj hasło: ")
        password2 = input("Powtórz hasło: ")
        if weryfikacja == 1:
            liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            kod = random.sample(liczby, 6)
            print(kod)
            email = str(input("Proszę podać email\n----> "))
            sender = 'BartekSando13@gmail.com'
            receivers = [email]
            print(receivers)
        elif weryfikacja == 2:
            pass
        else:
            print("Wpisano niewłaściwą liczbę, nie ustawiono weryfikacji dwuetapowej")
        if password != password2:
            print("Hasła się nie zgadzają!")
            continue
        else:
            status = 1
            print("Poprawnie zarejestrowano", login + "!")
            registration = False

while status == 1:
    while log:
        print("Proszę się zalogować")
        login2 = input("Podaj swój login: ")
        password3 = input("Podaj hasło: ")
        if login != login2 or password3 != password:
            print("Hasło albo login się nie zgadza!")
            continue
        else:
            print("Poprawnie zalogowano", login + "!")
            log = False
