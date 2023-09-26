# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 23:28:09 2023

@author: ygbal
"""

import tkinter as tk


ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

label1 = tk.Label(ventana, text="Fahrenheit:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=1)

button1 = tk.Button(ventana, text="Convertir a Celsius")#, command=convertir_a_celsius)
button1.grid(row=0, column=2)

label2 = tk.Label(ventana, text="Celsius:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1)

button2 = tk.Button(ventana, text="Convertir a Fahrenheit")#, command=convertir_fahrenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(ventana, text="Restablecer")#, command=borrar)
button3.grid(row=2, column=1)

ventana.mainloop()

