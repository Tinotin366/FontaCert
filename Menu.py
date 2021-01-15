#!/usr/bin/env python


import mariadb
# Python 3.8.6

import sys
import os
from Funciones import *
from conf import db
from Colors import bcolors

# import TitularDireccionCompletaListado
# Instalar pip install pynput # para captura de pulsacion de teclas

# # now, to cleaner the screen

cleaner()

# def pulsa(tecla):
# 	print('Se ha pulsado la tecla ' + str(tecla))
#
# with kb.Listener(pulsa) as escuchador:
# 	escuchador.join()

while True:
        Cabecera()
        # print('\n\t')
        # print (f'\n\t\t\t{bcolors.OkCyan}{bcolors.Bold}FontaCert:{bcolors.EndC} Programa de Gestion de Certificados de Fontaneria')
        # print ('\t\t___________________________________________________________________________')
        # print ('                                                                          ')

        print (f"\t \
                [1] {bcolors.OkBlue}Certificados{bcolors.EndC}\n\t\t \
            [11] {bcolors.OkGreen}Buscar Certificado{bcolors.EndC} \n\t\t \
            [12] {bcolors.OkGreen}Nuevo Certificado{bcolors.EndC}\n\t\t \
            [13] {bcolors.OkGreen}Editar Certificado{bcolors.EndC}\n\t\t \
            [14] {bcolors.OkGreen}Listado Certificados{bcolors.EndC}\n\t\t \
            [15] {bcolors.OkGreen}Eliminar Certificado{bcolors.EndC}\n\n\t \
                [2] {bcolors.OkBlue}Titulares{bcolors.EndC}\n\t\t \
            [21] {bcolors.OkGreen}Buscar Titular{bcolors.EndC}\n\t\t \
            [22] {bcolors.OkGreen}Nuevo Titular{bcolors.EndC}\n\t\t \
            [23] {bcolors.OkGreen}Editar Titular{bcolors.EndC}\n\t\t \
            [24] {bcolors.OkGreen}Listado Titulares{bcolors.EndC}\n\t\t \
            [25] {bcolors.OkGreen}Clonar Titular a Instalacion{bcolors.EndC}\n\t\t \
            [26] {bcolors.OkGreen}Eliminar Titular{bcolors.EndC}\n\n\t \
                [3] {bcolors.OkBlue}Instalaciones{bcolors.EndC}\n\t\t \
            [31] {bcolors.OkGreen}Buscar Instalacion{bcolors.EndC}\n\t\t \
            [32] {bcolors.OkGreen}Nueva Instalacion{bcolors.EndC}\n\t\t \
            [32] {bcolors.OkGreen}Editar Instalacion{bcolors.EndC}\n\t\t \
            [34] {bcolors.OkGreen}Listado Instalaciones{bcolors.EndC}\n\t\t \
            [35] {bcolors.OkGreen}Eliminar Instalacion{bcolors.EndC}\n\n\t \
                [4] {bcolors.OkBlue}Poblaciones, Municipios{bcolors.EndC}\n\t\t \
            [41] {bcolors.OkGreen}Buscar Poblacion{bcolors.EndC}\n\t\t \
            [42] {bcolors.OkGreen}Nueva Poblacion{bcolors.EndC}\n\t\t \
            [43] {bcolors.OkGreen}Editar Poblacion{bcolors.EndC}\n\t\t \
            [44] {bcolors.OkGreen}Listado Poblaciones{bcolors.EndC}\n\t\t \
            [44] {bcolors.OkGreen}Eliminar Poblacion{bcolors.EndC}\n\n\t \
                [5] {bcolors.OkBlue}Dotaciones{bcolors.EndC}\n\t\t \
            [51] {bcolors.OkGreen}Buscar Dotacion{bcolors.EndC}\n\t\t \
            [52] {bcolors.OkGreen}Nueva Dotacion{bcolors.EndC}\n\t\t \
            [53] {bcolors.OkGreen}Editar Dotacion{bcolors.EndC}\n\t\t \
            [54] {bcolors.OkGreen}Listado Dotaciones{bcolors.EndC}\n\t\t \
            [54] {bcolors.OkGreen}Eliminar Dotacion{bcolors.EndC}\n\n\t \
                [q] {bcolors.BgRed}Salir         {bcolors.EndC}")
                # [c]{bcolors.OkBlue} Limpiar{bcolors.EndC}\n\n\t \

        # print ('                                                                          ')

        print ('\n\t\t___________________________________________________________________________')

        opcion = input("\n\t\t Opcion: ")

        if opcion == "1":
            os.system("/usr/bin/python Certificados.py")

        if opcion == "11":
            os.system("/usr/bin/python Buscar_Certificado.py")

        if opcion == "12":
            os.system("/usr/bin/python Nuevo_Certificado.py")

        if opcion == "13":
            os.system("/usr/bin/python Edicion_Certificado.py")

        if opcion == "14":
            os.system("/usr/bin/python Listado_Certificados.py")

        if opcion == "15":
            os.system("/usr/bin/python Eliminar_Certificado.py")


        if opcion == "2":
            os.system("/usr/bin/python Titulares.py")

        if opcion == "21":
            os.system("/usr/bin/python Busqueda_Titular.py")

        if opcion == "22":
            os.system("/usr/bin/python Nuevo_Titular.py")

        if opcion == "23":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "24":
            os.system("/usr/bin/python Listado_Titulares.py")

        if opcion == "25":
            os.system("/usr/bin/python Desarrollo.py")
            # os.system("/usr/bin/python Clonar_Titulares2Instalacion.py")

        if opcion == "26" or opcion == "2":
            os.system("/usr/bin/python Eliminar_Titular.py")


        if opcion == "3":
            os.system("/usr/bin/python Instalaciones.py")

        if opcion == "31":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "32":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "33":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "4":
            os.system("/usr/bin/python Poblaciones.py")

        if opcion == "41":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "42":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "43":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "44":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "45":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "5":
            os.system("/usr/bin/python Dotaciones.py")

        if opcion == "51":
            os.system("/usr/bin/python Listado_Dotacion.py")

        if opcion == "52":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "53":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "54":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == "55":
            os.system("/usr/bin/python Desarrollo.py")

        if opcion == 'C' or opcion == 'c':
            cleaner()

        if opcion == 'Q' or opcion == 'q':
            break
