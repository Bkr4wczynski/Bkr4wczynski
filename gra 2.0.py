from random import randrange
level = int(input("Wybierz poziom: 1-łatwy(1-100) 2-średni(1-1000) 3-trudny(1-10 000): "))
if level == 1:
    number = randrange(100)
elif level == 2:
    number = randrange(1000)
elif level == 3:
    number = randrange(10000)
else:
    number = randrange(1000)
while True:
    shoot = int(input("Podaj liczbę: "))
    if shoot == number:
        print("Wygrałeś!")
        break
    elif shoot > number:
        print("Za duża!")
    else:
        print("Za mała")
