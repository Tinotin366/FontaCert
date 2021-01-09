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



# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
# Titulares = [0, "NombreTitular", "CIFNIF"]
cur = ConnectDB.cursor()
# Ejecucion de la consulta
# cur.execute(
# "SELECT Titulares.Id_Titular, Titulares.CIFNIF, Titulares.NombreTitular, TitularesDireccion.Id_Via, TitularesDireccion.NombreVia, TitularesDireccion.Numero, TitularesDireccion.Escalera, TitularesDireccion.Piso, TitularesDireccion.Puerta, TitularesDireccion.Id_Municipio FROM Titulares, TitularesDireccion WHERE  Titulares.Id_Titular = TitularesDireccion.Id_Titular",
# )

cur.execute(
"SELECT Titulares.Id_Titular, CIFNIF, NombreTitular, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta, Id_Municipio FROM Titulares, TitularesDireccion WHERE  Titulares.Id_Titular = TitularesDireccion.Id_Titular",
)

# Print Result-set (Conjunto Resultante)

print("IdTitular  CIFNIF   \t Titular  Via Id_Via NombreVia                           Numero Escalera Piso Puerta Id Municipio"   )

for (Id_Titular, CIFNIF, NombreTitular, Id_Via, NombreVia, Numero, Escalera, Piso, Puerta, Id_Municipio) in cur:
    print(f"{Id_Titular} \t {CIFNIF} \t   {NombreTitular}  {Id_Via} {NombreVia}, {Numero}, {Escalera}, {Piso}, {Puerta},  {Id_Municipio}"   )
