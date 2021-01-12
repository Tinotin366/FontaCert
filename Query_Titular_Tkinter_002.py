#!/usr/bin/env python


import mariadb
import tkinter as tk
from tkinter import ttk

# Python 3.8.6
# Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.
import sys
from conf import db

# Instanciar Connection

try:
   ConnectDB = mariadb.connect (
        host=db[0], port=db[1], user=db[2], password=db[3], database=db[4]
        )
except mariadb.Error as e:
    print(f"Error conectando a la Plataforma MariaDB: {e}")
    sys.exit(1)



Titulares = tk.Tk()


# Titulares.resizable(0,0)
Titulares.geometry("1200x600")

TitularesForm= tk.Label(Titulares,text =("Consulta de Titulares de los Certificados"),font=("Sans",18))
TitularesForm.place(relx=0.05 ,rely=0.05)

def QueryTitulares():

    Titulares.title ("Titulares de los Certificados")
    Titular = Toplevel(root)
    Titular.title('View all customers')

    Cur = con.cursor()

    Cur.execute("SELECT Id_Titular, CIFNIF, Titular FROM Titulares;")
    result = Cur.fetchall()

    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(Titular, text=y)
            lookup_label.grid(row=index+1, column=num)
            num +=1
    print("Aqui estoy")
    l1 = Label(Titular,text='IdTitular',font=font_text)
    l2 = Label(Titular,text='CIFNIF',font=font_text)
    l3 = Label(Titular,text='Titular',font=font_text)

    btn_ext = Button(Titular,text='Exit',font=font_text,command=log.destroy,borderwidth=2,fg='#eb4d4b')
    l1.grid(row=0,column=0,padx=20)
    l2.grid(row=0,column=1,padx=20)
    l3.grid(row=0,column=2,padx=20)

    btn_ext.grid(row=index+2,columnspan=3,ipadx=540)

# # Print Result-set (Conjunto Resultante)
# for (IdTitular, CIFNIF, Titular) in cur:
#     print(f"IdTitular: {IdTitular} \t CIFNIF:      {CIFNIF} \t   Nombre Titular: {Titular}"   )

Titulares.mainloop()
