import tkinter

root = tkinter.Tk()
root.geometry('800x600+300+300')
root.config(bg='lightgrey')
root.title('Python Clicker')

napis = tkinter.Label(root, text='PythonSimpleClicker :)')
napis.pack()

clicks = tkinter.IntVar()

def add_numbers():
    clicks.set(clicks.get()+1)
    lb.config(text=f'Kliknąłeś mnie: {clicks.get()} razy!')


lb = tkinter.Label(text=f'Kliknięto Mnie: {clicks.get()}')
lb.pack(side=tkinter.TOP)

button = tkinter.Button(root, text='Kliknij mnie',command= add_numbers, height=10, width=20, bg= 'grey')
button.pack()

root.mainloop()
