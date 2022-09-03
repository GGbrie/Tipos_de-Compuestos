def  cargar ():
    productos = {}
    for  x  in  rango ( 5 ):
        nombre = input ( "Ingrese el nombre del producto:" )
        precio = int ( input ( "Ingrese el precio:" ))
        productos [ nombre ] = precio
    devolver  productos


def  imprimir ( productos ):
    print ( "Listado de todos los articulos" )
    por  nombre  en  productos :
        imprimir ( nombre , productos [ nombre ])


def  imprimir_mayor100 ( productos ):
    print ( "Listado de articulos con precios mayores a 100" )
    por  nombre  en  productos :
        si  productos [ nombre ] > 100 :
            imprimir ( nombre )

            
# bloque principal

productos = cargar ()
imprimir ( productos )
imprimir_mayor100 ( productos )
