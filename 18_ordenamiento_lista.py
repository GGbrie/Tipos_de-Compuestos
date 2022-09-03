sueldos = []
para  x  en  rango ( 5 ):
    valor = int ( input ( "Ingrese sueldo:" ))
    sueldos _ agregar ( valor )

print ( "Lista sin ordenar" )
imprimir ( sueldos )

para  x  en  rango ( 4 ):
    si  sueldos [ x ] > sueldos [ x + 1 ]:
        aux = sueldos [ x ]
        sueldos [ x ] = sueldos [ x + 1 ]
        sueldos [ x + 1 ] = aux

print ( "Lista con el último elemento ordenado" )
imprimir ( sueldos )
