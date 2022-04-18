import tkinter as tk

symbole = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(', ')', '1', '2', '3', '-', 'x²', '\u221A',
           '0', ',', '%', '+']

COLOR = "#f2f4f7"


def inicjalizacjaOkienka():
    root = tk.Tk()

    root.configure(bg=COLOR)
    app_sixe_x = 470
    app_sixe_y = 430
    root.geometry(f"{app_sixe_x}x{app_sixe_y}")
    root.maxsize(app_sixe_x,app_sixe_y)
    root.title('Kalkulator')
    root.maxsize()

    return root

def inicjalizacjaEkranu(root):
    ekran = [
        tk.Label(root, width=65, bg='#D3D3D3', text='', anchor='w', borderwidth=2)
        for i in range(3)
    ]

    for i in range(len(ekran)):
        ekran[i].grid(row=i, columnspan=6, ipady=15,ipadx=1)

    return ekran


def inicjalizacjaPolaDanych(root, ekran):

    pole_na_dane = tk.Entry(
        root, borderwidth=0, highlightcolor='white', highlightbackground='white'
    )
    pole_na_dane.grid(row=len(ekran), columnspan=6, ipadx=169, ipady=10)

    info = tk.Label(root, width=65, bg='white', text='', anchor='w', borderwidth=0)
    info.grid(row=len(ekran) + 1, columnspan=6, ipady=15,ipadx=1)

    return pole_na_dane, info


def przycsikKlik(pole_na_dane, symbol):
    def f():
        if symbol == "\u21BA":
            bufor = pole_na_dane.get()[:-1]
            pole_na_dane.delete(0, tk.END)
            pole_na_dane.insert(0, bufor)

        elif symbol == "C":
            pole_na_dane.delete(0, tk.END)

        else:
            tekst = symbol if symbol != "x²" else "^2"
            pole_na_dane.insert(tk.END, tekst)

    return f


def oblicz(pole_na_dane, ekran, info):
    def czyPoprawnyOstatniZnak(tekst):
        i = 1

        while tekst[-i] == ")":
            i += 1

        return tekst[-i].isdigit()

    def czyWielokrotneOperatory(tekst):

        for i in range(len(tekst)):
            if not tekst[i].isdigit() and not tekst[i + 1].isdigit():
                return True

        return False

    def zamienZnakPotegi(tekst):

        for i in range(len(tekst)):
            if tekst[i] == "^":
                tekst = tekst[:i] + "**" + tekst[i + 1 :]

        return tekst

    def f():
        tekst = pole_na_dane.get()

        if not czyPoprawnyOstatniZnak(tekst) or czyWielokrotneOperatory(tekst):
            info["text"] = "Bledne wyrazenie"

        else:

            for i in range(1, len(ekran)):
                if ekran[i]["text"]:
                    ekran[i - 1]["text"] = ekran[i]["text"]

            if "^" in tekst:
                wyrazenie = zamienZnakPotegi(tekst)
                ekran[-1]["text"] = tekst + " = " + str(eval(wyrazenie))

            else:
                ekran[-1]["text"] = tekst + " = " + str(eval(tekst))

    return f


def inicjalizacjaPrzyciskow(root, ekran, info):
    przyciski = [
        tk.Button(root, text=symbol, bg=COLOR, borderwidth=0, width=3, highlightbackground='RoyalBlue3',
                  font='Havletica', relief=tk.SUNKEN) for symbol in symbole
    ]

    j = len(ekran) + 2
    for i in range(len(przyciski)):
        if i % 6 == 0:
            j += 1

        margin = 21 if len(symbole[i]) == 1 else 10
        przyciski[i].grid(row=j, column=i % 6, ipady=5, ipadx=margin)
        przyciski[i].configure(command=przycsikKlik(pole_na_dane, przyciski[i]["text"]))


    znak_rownosc = tk.Button(root, text='=', bg='#969696', borderwidth=0.5, relief=tk.RAISED,command=oblicz(pole_na_dane, ekran, info))
    znak_rownosc.grid(row=len(ekran) + 6, column=4, columnspan=2, ipady=5, ipadx=50)

    return przyciski


if __name__ == "__main__":

    root = inicjalizacjaOkienka()

    ekran = inicjalizacjaEkranu(root)

    pole_na_dane, info = inicjalizacjaPolaDanych(root, ekran)

    przyciski = inicjalizacjaPrzyciskow(root, ekran, info)

    root.mainloop()
