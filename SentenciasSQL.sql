select  Titulares.Id_Titular, Titulares.Titular,Titulares.CIFNIF, \
        TitularesDireccion.Id_Via, TitularesDireccion.NombreVia, TitularesDireccion.Numero, \
        TitularesDireccion.Escalera, TitularesDireccion.Piso, TitularesDireccion.Puerta, TitularesDireccion.Id_Municipio \
         from Titulares, TitularesDireccion \
         where Titulares.Id_Titular = TitularesDireccion.Id_Titular;

# Desarrollo

INNER JOIN Municipios ON TitularesDireccion.Id_Municipio = Municipios.Id_Municipio;

# Cuando hay que sustituir con campos con un valor Null

UPDATE TitularesDireccion SET TitularesDireccion.Id_Via = "Cl" where Id_Via IS NULL;

SELECT * FROM Municipios WHERE CP LIKE '296%';

SELECT TitularesDireccion.Id_Titular, Municipios.Poblacion, Municipios.Municipio, Municipios.CP  \
FROM TitularesDireccion INNER JOIN Municipios ON  TitularesDireccion.Id_Poblacion =  Municipios.CP;

SELECT Titulares.Id_Titular, Titulares.Titular, Titulares.CIFNIF, TitularesDireccion.Id_Via, \
TitularesDireccion.NombreVia, TitularesDireccion.Numero, TitularesDireccion.Escalera, TitularesDireccion.Piso,\
 TitularesDireccion.Puerta, Municipios.Poblacion, Municipios.Municipio, Municipios.CP \
  FROM  Titulares, TitularesDireccion LEFT JOIN Municipios ON  TitularesDireccion.Id_Poblacion =  Municipios.Id_Poblacion \
  WHERE Titulares.Id_Titular = TitularesDireccion.Id_Direccion;

SET  @Search = '%Mar%'; SELECT Id_Titular, CIFNIF, Titular FROM Titulares WHERE Titular  LIKE @Search OR CIFNIF LIKE @Search;
