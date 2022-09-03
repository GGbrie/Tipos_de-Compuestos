lista = [[ 1 ], [ 1 , 2 ], [ 1 , 2 , 3 ], [ 1 , 2 , 3 , 4 ], [ 1 , 2 , 3 , 4 , 5 ]]

suma = 0
para  k  en  rango ( len ( lista )):
    para  x  en  rango ( len ( lista [ k ])):
        suma = suma + lista [ k ][ x ]
imprimir ( suma )
