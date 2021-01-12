import os
from Colors import bcolors

def Cabecera():
        print('\n\t')
        print (f'\n\t\t\t{bcolors.OkCyan}{bcolors.Bold}FontaCert:{bcolors.EndC} Programa de Gestion de Certificados de Fontaneria')
        print ('\t\t___________________________________________________________________________')
        print ('                                                                          ')

def cleaner():
    os.system('cls()' if os.name=='nt' else 'clear')

def pause():
    Pausar = input("\n\n\t\tPulsa la tecla <ENTER>  para ir al Menu...")

def desarrollo():
    print("\n\t\t\tEsta Funcion todavia no esta implementada")
