def  cargar ():
    agenda = {}
    continuo1 = "s"
    mientras  continua1 == "s" :
        fecha = input ( "ingrese la fecha con formato dd/mm/aa:" )
        continuo2 = "s"
        lista = []
        mientras  continua2 == "s" :
            hora = input ( "Ingrese la hora de la actividad con formato hh:mm " )
            actividad = input ( "Ingrese la descripción de la actividad:" )
            lista _ agregar (( hora , actividad ))
            continua2 = input ( "Ingresa otra actividad para la misma fecha[s/n]:" )
        agenda [ fecha ] = lista
        continua1 = entrada ( "Ingresa otra fecha[s/n]:" )
     programa de regreso


def  imprimir ( agenda ):
    print ( "Lista completa de la agenda" )
    para  fecha  en  agenda :
        print ( "Para la fecha:" , fecha )
        para  hora , actividad  en  agenda [ fecha ]:
            imprimir ( hora , actividad )


def  consulta_fecha ( agenda ):
    fecha = input ( "Ingrese la fecha que desea consultar:" )
    si  fecha  en  agenda :
        para  hora , actividad  en  agenda [ fecha ]:
            imprimir ( hora , actividad )
    más :
        print ( "No hay actividades agendadas para dicha fecha" )
            

# bloque principal

agenda = cargar ()
imprimir ( agenda )
consulta_fecha ( agenda )
