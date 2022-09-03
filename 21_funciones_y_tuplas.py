def  cargar_fecha ():
    dd = int ( input ( "Ingrese numero de dia:" ))
    mm = int ( input ( "Ingrese numero de mes:" ))
    aa = int ( input ( "Ingrese numero de año:" ))
    retorno ( dd , mm , aa )


def  imprimir_fecha ( fecha ):
    imprimir ( fecha [ 0 ], fecha [ 1 ], fecha [ 2 ], sep = "/" )


# bloque principal

fecha = cargar_fecha ()
imprimir_fecha ( fecha )
