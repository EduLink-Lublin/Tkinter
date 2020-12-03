from tkinter import *
from tkinter.ttk import *

def odpal_okno():
    main_window = Tk()

    main_window.title("Nazwa okna")
    label = Label(main_window, text="Wyświetlamy w oknie").pack()
    # label2 = Label(main_window, text="Wyświetlamy w okni").pack()

    main_window.mainloop()


