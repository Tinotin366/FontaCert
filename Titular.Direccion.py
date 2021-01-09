#!/usr/bin/env python


import mariadb
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


ConnectDB.autocommit = False
# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "NombreTitular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta

print ("Nuevo Titular")

# Creacioin de la Variable de entrada para poder insertarla en la base de datos de TitularesForm

def Titulares():
# Tabla Titulares

    Id_Titular = int(input("ID del Titular: "))
    CIFNIF = str(input("CIF/NIF: "))
    NombreTitular= str(input("Nombre del Titular: "))

    # Tabla Direcciones Titulares

    # Direcciones
    # Id_Direccion = int(input("

    Id_Direccion = Id_Titular                       # Direccion[0]
    Id_Via = str(input("Tipo Via: "))               # Direccion[1]
    NombreVia = str(input("Nombre de la Via: "))    # Direccion[2]
    Numero = int(input("Numero: "))                 # Direccion[3]
    Escalera = str.upper(str(input("Escalera: ")))             # Direccion[4]
    Piso = str(input("Piso: "))                     # Direccion[5]
    Puerta = str.upper(str(input("Puerta: ")))                 # Direccion[6]
    Id_Poblacion = int(input("Codigo Poblacion: ")) # Direccion[7]

    Id_Municipio = Id_Poblacion



    Titular = [Id_Titular, CIFNIF, NombreTitular]
    Direccion = [Id_Direccion, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta, Id_Poblacion]

    print(Titular[0])
    print (f"Los datos introducidos son: \n Titular: {Titular[0]} \n CIFNIF:      {Titular[1]} \n   Nombre Titular: {Titular[2]}")

    SentenciaInsertSQL = "INSERT INTO Titulares (Id_Titular, CIFNIF, NombreTitular) VALUES (%s,%s,%s)"
    DatosInsertSQL =(Titular[0],Titular[1],Titular[2])
    print(DatosInsertSQL)
    # print(str(SentenciaInsertSQL))
    # (Titular[0],Titular[1],Titular[2])
    cur.execute(SentenciaInsertSQL,DatosInsertSQL)

    SentenciaInsertSQL = "INSERT INTO TitularesDireccion (Id_Titular, Id_Direccion,  Id_Via,         NombreVia,      Numero,         Escalera,       Piso,           Puerta,         Id_Poblacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    DatosInsertSQL = (Titular[0], Direccion[0],    Direccion[1],   Direccion[2],   Direccion[3],   Direccion[4],   Direccion[5],   Direccion[6],   Direccion[7])

    cur.execute(SentenciaInsertSQL,DatosInsertSQL)

    ConnectDB.commit()
    print (f"\n Actualizada Direccion del Titular del Titular nº: {Titular[0]}")

NuevoRegistro= 'S'

while NuevoRegistro == 'S':
    Titulares()
    NuevoRegistro = str.upper(str(input("Nuevo Registro (S/N): ")))
else:
    sys.exit()

cur.close()
ConnectDB.close()

# Poner para solicitar si nuevo registro o Salir
