# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 23:28:09 2023

@author: ygbal
"""

import tkinter as tk

def convertir_a_celsius():
    Fahrenheit = float(entry1.get())
    #Celsius = (Fahrenheit-32)*5.0/9.0
    Celsius = (Fahrenheit-32)*5/9
    entry2.delete(0, tk.END)
    entry2.insert(0,f"{Celsius:.2f}")

def convertir_a_fahrenheit():
    Celsius = float(entry2.get())
    #Celsius = (Fahrenheit-32)*5.0/9.0
    Fahrenheit = (Celsius*9/5)+32
    entry1.delete(0, tk.END)
    entry1.insert(0,f"{Fahrenheit:.2f}")
def borrar():
    entry1.delete(0,tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0,tk.END)
    entry2.insert(0, "0.0")

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

label1 = tk.Label(ventana, text="Fahrenheit:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=1)

button1 = tk.Button(ventana, text="Convertir a Celsius", command=convertir_a_celsius)
button1.grid(row=0, column=2)

label2 = tk.Label(ventana, text="Celsius:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1)

button2 = tk.Button(ventana, text="Convertir a Fahrenheit", command=convertir_a_fahrenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(ventana, text="Restablecer", command=borrar)
button3.grid(row=2, column=1)

ventana.mainloop()