lista = [[ 1 , 1 , 1 , 1 , 1 ], [ 2 , 2 , 2 , 2 , 2 ]]

suma1 = lista [ 0 ][ 0 ] + lista [ 0 ][ 1 ] + lista [ 0 ][ 2 ] + lista [ 0 ][ 3 ] + lista [ 0 ][ 4 ]
imprimir ( suma1 )
suma2 = lista [ 1 ][ 0 ] + lista [ 1 ][ 1 ] + lista [ 1 ][ 2 ] + lista [ 1 ][ 3 ] + lista [ 1 ][ 4 ]
imprimir ( suma2 )
imprimir ( "----------" )

suma1 = 0
para  x  en  rango ( len ( lista [ 0 ])):
    suma1 = suma1 + lista [ 0 ][ x ]
suma2 = 0
para  x  en  rango ( len ( lista [ 1 ])):
    suma2 = suma2 + lista [ 1 ][ x ]
imprimir ( suma1 )
imprimir ( suma2 )
imprimir ( "----------" )

para  k  en  rango ( len ( lista )):
    suma = 0
    para  x  en  rango ( len ( lista [ k ])):
        suma = suma + lista [ k ][ x ]
    imprimir ( suma )
