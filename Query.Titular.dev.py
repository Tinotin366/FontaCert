#!/usr/bin/env python



import json
import sys
# import ConnectMariaDB as Connect
with open("MariaDB.json") as json_data_file:
    data = json.load(json_data_file)
print(data)


# import mariadb
# # Python 3.8.6
# # Conectar a la plataforma MariaDB utilizando la función connect () con los atributos relevantes.

#
# # Instanciar Connection
try:
   ConnectDB = mariadb.connect()


except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")


sys.exit(1)
#


# Cree un cursor llamando al método cursor () en la conexión:

# Instanciar Cursor (Cursor de instancia)
# Obtener Cursor
Titulares = [0, "NombreTitular", "CIFNIF"]
cur = ConnectDB.cursor()

cur.execute("SELECT Id_Titular, NombreTitular, CIFNIF FROM Titular;",)
#
# Print Result-set
for (IdTitular, NombreTitular,CIFNIF) in cur:
    print(f"IdTitular: {IdTitular}, Nombre Titular: {NombreTitular}, CIFNIF {CIFNIF}")
