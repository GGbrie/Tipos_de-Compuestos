def  cargar ():
    diccionario = {}
    continuo = "s"
    mientras  continua == "s" :
        casta = input ( "Ingrese palabra en castellano:" )
        ing = input ( "Ingrese palabra en ingles:" )
        diccionario [ esp ] = casta
        continua = input ( "Quiere cargar otra palabra:[s/n]" )
    volver  diccionario


def  imprimir ( diccionario ):
    print ( "Listado completo del diccionario" )
    para  ingles  en  diccionario :
        imprimir ( ingles , diccionario [ ingles ])


def  consultar_palabra ( diccionario ):
    pal = input ( "Ingrese la palabra en ingles a consultar:" )
    si  amigo  en  el diccionario :
        print ( "En castellano significa:" , diccionario [ pal ])


# bloque principal

diccionario = cargar ()
imprimir ( diccionario )
consulta_palabra ( diccionario )
