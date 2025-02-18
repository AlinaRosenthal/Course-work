from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Geometry calculator")
window.geometry('400x200')

frm = ttk.Frame(window, padding=10)
frm.grid()

label = ttk.Label(frm, text="Выберите, для какой фигуры будет расчёт")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

ttk.Button(frm, text="Двумерная (на плоскости)", command=window.destroy).grid(row=1, column=0, padx=10, pady=10)
ttk.Button(frm, text="Трёхмерная (в пространстве)", command=window.destroy).grid(row=1, column=1, padx=10, pady=10)

window.mainloop()