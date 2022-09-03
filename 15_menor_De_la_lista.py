lista = []
para  x  en  rango ( 5 ):
    valor = int ( input ( "Ingrese valor:" ))
    lista _ agregar ( valor )

menor = lista [ 0 ]
posición = 0
para  x  en  rango ( 1 , 5 ):
    si  lista [ x ] < menor :
        menor = lista [ x ]
        posicion = x

imprimir ( "Lista completa" )
imprimir ( lista )
print ( "Menor de la lista" )
imprimir ( menor )
print ( "Posición del menor en la lista" )
imprimir ( posición )
