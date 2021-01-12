import os


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def pause():
    Pausar = input("\n\n\t\tPulsa la tecla <ENTER>  para ir al Menu...")
