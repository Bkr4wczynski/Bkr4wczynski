import sys
login = input("Podaj login: ")
password = input("Podaj hasło: ")
password2 = input("Powtórz hasło: ")

if password != password2:
    sys.exit("Hasła się nie zgadzają! ")
else:
    print("Poprawnie zalogowano, witaj", login + "!")
    file = open("Hasło.txt", "a")
    file.write("Haslo to: \n")
    file.write(password)
    file.write("\nLogin to: ")
    file.write(login)
    file.close()

