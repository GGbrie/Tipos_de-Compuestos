def  cargar ():
    empleados = []
    para  x  en  rango ( 5 ):
        nombre = input ( "Nombre del empleado:" )
        sueldo = int ( input ( "Ingrese el sueldo:" ))
        empleados _ agregar (( nombre , sueldo ))
    volver  empleados


def  imprimir ( empleados ):
    print ( "Listado de los nombres de empleados y sus sueldos" )
    for  nombre , sueldo  en  empleados :
        imprimir ( nombre , sueldo )


def  mayor_sueldo ( empleados ):
    empleado = empleados [ 0 ]
    para  emp  en  empleados :
        si  emp [ 1 ] > empleado [ 1 ]:
            empleado = emp
    print ( "Empleado con mayor sueldo:" , empleado [ 0 ], "su sueldo es" , empleado [ 1 ])


def  sueldos_menor1000 ( empleados ):
    no puedo = 0
    para  empleado  en  empleados :
        si  empleado [ 1 ] < 1000 :
            no puedo = no puedo + 1    
    print ( "Cantidad de empleados con un sueldo menor a 1000 son:" , cant )
    

# bloque principal

empleados = cargar ()
imprimir ( empleados )
mayor_sueldo ( empleados )                        
sueldos_menor1000 ( empleados )
