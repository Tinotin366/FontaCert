#!/usr/bin/env python


import mariadb
# Python 3.8.6
# Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.
import sys
import os
from conf import db
from Colors import bcolors

# import TitularDireccionCompletaListado
# Instalar pip install pynput # para captura de pulsacion de teclas


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

# def pulsa(tecla):
# 	print('Se ha pulsado la tecla ' + str(tecla))
#
# with kb.Listener(pulsa) as escuchador:
# 	escuchador.join()

cls()


while True:
        print('\n\t')
        print (f'\n\t\t\t{bcolors.OkCyan}{bcolors.Bold}FontaCert:{bcolors.EndC} Programa de Gestion de Certificados de Fontaneria')
        print ('\t\t___________________________________________________________________________')
        print ('                                                                          ')

        print (f"\
            \t\t[1]{bcolors.OkBlue} Certificados{bcolors.EndC}\n\t\t \
            [11] {bcolors.OkGreen}Buscar Certificados{bcolors.EndC} \n\t\t \
            [12] {bcolors.OkGreen}Nuevo Certificados{bcolors.EndC}\n\t\t \
            [13] {bcolors.OkGreen}Editar Certificados{bcolors.EndC}\n\t\t \
            [14] {bcolors.OkGreen}Eliminar Certificados{bcolors.EndC}\n\t\t \
            [15] {bcolors.OkGreen}Listado Completo Certificados{bcolors.EndC}\n\n\t \
                [2]{bcolors.OkBlue} Titulares{bcolors.EndC}\n\t\t \
            [21] {bcolors.OkGreen}Buscar Titular{bcolors.EndC}\n\t\t \
            [22]{bcolors.OkGreen} Nuevo Titular{bcolors.EndC}\n\t\t \
            [23] {bcolors.OkGreen}Editar Titular{bcolors.EndC}\n\t\t \
            [24] {bcolors.OkGreen}Eliminar Titular{bcolors.EndC}\n\t\t \
            [25] {bcolors.OkGreen}Listado Completo Titulares{bcolors.EndC}\n\n\t \
                [3] {bcolors.OkBlue}Instalaciones{bcolors.EndC}\n\t\t \
            [31]{bcolors.OkGreen} Buscar Instalacion{bcolors.EndC}\n\t\t \
            [32] {bcolors.OkGreen}Nueva Instalacion{bcolors.EndC}\n\t\t \
            [32] {bcolors.OkGreen}Editar Instalacion{bcolors.EndC}\n\n\t \
                [4]{bcolors.OkBlue} Poblaciones, Municipios{bcolors.EndC}\n\t\t \
            [41] {bcolors.OkGreen}Buscar Poblaciones{bcolors.EndC}\n\t\t \
            [42] {bcolors.OkGreen}Nueva Poblacion{bcolors.EndC}\n\t\t \
            [43] {bcolors.OkGreen}Editar Poblacion{bcolors.EndC}\n\n\t \
                [5] {bcolors.OkBlue}Dotaciones{bcolors.EndC}\n\t\t \
            [51] {bcolors.OkGreen}Buscar Dotacion{bcolors.EndC}\n\t\t \
            [52] {bcolors.OkGreen}Nueva Dotacion{bcolors.EndC}\n\t\t \
            [53] {bcolors.OkGreen}Editar Dotacion{bcolors.EndC}\n\n\t \
                [c]{bcolors.OkBlue} Limpiar{bcolors.EndC}\n\n\t \
                [q] {bcolors.BgRed}Salir         {bcolors.EndC}")
        print ('                                                                          ')

        print ('\n\t\t___________________________________________________________________________')

        opcion = input("\n\t\t Opcion: ")
        if opcion == "1":
            cls()
            os.system("/usr/bin/python CertificadosListado.py")

        if opcion == "2":
            cls()
            os.system("/usr/bin/python TitularListado.py")

        if opcion == "3":
            cls()
            print('\n\tTitulares Direcciones')

        if opcion == "25" or opcion == "2":
            cls()
            os.system("/usr/bin/python TitularDireccionCompletaListado.py")

        if opcion == "21":
            cls()
            os.system("/usr/bin/python TitularNuevo.py")

        if opcion == 'C' or opcion == 'c':
            cls()

        if opcion == 'Q' or opcion == 'q':
            break
