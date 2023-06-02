import tkinter as tk
from tkinter import * 
from tkinter import ttk


Ventana = Tk()
Ventana.title("ADMINISTRACION DE ALMACEN DE BEBIDAS")
Ventana.geometry("520x480")
Ventana.config(bg="SpringGreen3")

panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)

label = Label(pestaña1,text="Registrar una bebida",font=("Arial",20)).pack()


label1 = Label(pestaña1,text="Ingresa su ID",font="Arial").pack()
txt1 = tk.Entry(pestaña1).pack()

label2 = Label(pestaña1,text="Ingresa su Nombre",font="Arial").pack()
txt2 = tk.Entry(pestaña1).pack()

label3 = Label(pestaña1,text="Ingresa su Precio",font="Arial").pack()
txt3 = tk.Entry(pestaña1).pack()

label4 = Label(pestaña1,text="Ingresa su Clasificacion",font="Arial").pack()
txt4 = tk.Entry(pestaña1).pack()

label4 = Label(pestaña1,text="Ingresa su Marca",font="Arial").pack()
txt4 = tk.Entry(pestaña1).pack()

panel.add(pestaña1, text='Insertar una mercancia')

Ventana.mainloop()