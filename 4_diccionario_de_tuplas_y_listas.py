def  cargar ():
    productos = {}
    continuo = "s"
    mientras  continua == "s" :
        codigo = int ( input ( "Ingrese el codigo del producto:" ))
        descripcion = input ( "Ingrese la descripcion:" )
        precio = float ( input ( "Ingrese el precio:" ))
        stock = int ( input ( "Ingrese el stock real:" ))
        productos [ codigo ] = ( descripcion , precio , stock )
        continua = input ( "¿Desea cargar otro producto[s/n]?" )
    devolver  productos


def  imprimir ( productos ):
    print ( "Listado completo de productos:" )
    para  codigo  en  productos :
        print ( codigo , productos [ codigo ][ 0 ], productos [ codigo ][ 1 ], productos [ codigo ][ 2 ])


definitivamente  consultar ( productos ):
    codigo = int ( input ( "Ingrese el codigo de articulo a consultar:" ))
    si  codigo  en  productos :
        print ( productos [ código ][ 0 ], productos [ código ][ 1 ], productos [ código ][ 2 ])
        

def  listado_stock_cero ( productos ):
    print ( "Listado de articulos con stock en cero:" )
    para  codigo  en  productos :
        if  productos [ codigo ][ 2 ] == 0 :
            print ( codigo , productos [ codigo ][ 0 ], productos [ codigo ][ 1 ], productos [ codigo ][ 2 ])



# bloque principal

productos = cargar ()
imprimir ( productos )
consultar ( productos )
listado_stock_cero ( productos )
