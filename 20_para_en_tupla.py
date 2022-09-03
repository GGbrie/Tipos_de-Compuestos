def  cargar ():
    lista = []
    para  x  en  rango ( 5 ):
        num = int ( input ( "Ingrese un valor:" ))
        lista _ agregar ( num )
    volver  lista


def  imprimir ( lista ):
    imprimir ( "Lista completa" )
    para  elemento  en  lista :
        imprimir ( elemento )


def  mayor ( lista ):
    mayo = lista [ 0 ]
    para  elemento  en  lista :
        si  elemento > puede :
            mayo = elemento
    print ( "El elemento mayor de la lista es" , may )            
        

def  sumar_elementos ( lista ):
    suma = 0
    para  elemento  en  lista :
        suma = suma + elemento
    print ( "La suma de todos sus elementos es" , suma )


# bloque principal

lista = cargar ()
imprimir ( lista )
alcalde ( lista )
sumar_elementos ( lista )
