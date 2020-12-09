from tkinter import *
from tkinter.ttk import *
import time

def test():
    # zainicjowanie okan
    main_window = Tk()

    # dodanie nazwy okna i napisu w oknie
    main_window.title("Nazwa okna")
    label = Label(main_window, text="Pasek lata z lewej do prawej i z powrotem").pack(pady=10)

    # zdefiniowanie paska postępu i jego wywołanie
    progress = Progressbar(main_window, orient=HORIZONTAL, length=500, mode='determinate')
    progress.pack(pady=10)

    # deklaracja zmennych pomocniczych
    i = 0
    temp = 0

    # delkaracja nieskoczonej pętli
    while 1:
        # delkaracja warunku, który sprawdza czy iść dalej z paskiem
        # aktualizuje pasek postępu
        if temp == 0:
            i += 1
            progress['value'] = i
            main_window.update_idletasks()
            time.sleep(0.1)
            if i == 10:
                temp = 1
        # deklaracja warunku, który sprawdza czy pasek postępu może się już cofać
        # skraca pasek postępu
        elif temp == 1:
            i -= 1
            progress['value'] = i
            main_window.update_idletasks()
            time.sleep(0.1)
            if i == 0:
                temp = 0
            Button(main_window, text="QUIT", command=main_window.destroy).pack()
        # !! Podczas trwania tego nie można wyjść ani Buttonem ani X. Trzeba przez command line
        # ?? Potencjalne naprawienie asynchroniczność ??




    # wywołanie okna
    main_window.mainloop()