#!/usr/bin/env python



import json
import sys
# import ConnectMariaDB as Connect
with open("MariaDB.json") as json_data_file:
    data = json.load(json_data_file)
print(data)


# import mariadb
# # Python 3.8.6
# 

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
Titulares = [0, "Titular", "CIFNIF"]
cur = ConnectDB.cursor()

cur.execute("SELECT Id_Titular, Titular, CIFNIF FROM Titular;",)
#
# Print Result-set
for (IdTitular, Titular,CIFNIF) in cur:
    print(f"IdTitular: {IdTitular}, Nombre Titular: {Titular}, CIFNIF {CIFNIF}")
