
# function que va a listar las materias desaprobadas. 
# Recibe dni como parametro que es algo con un formato numerico estilo 11222333 
def desaprobadas(dni):

  # El archivo a leer es del formato dni.csv por eso concatenamos .csv al 
  # parametro dni

  filename = dni+".csv"

  # abrimos el archivo dni.csv en modo lectura ( 'r' ) 

  with open(filename, mode ='r')as file:

     # inicializamos una variable que nos permitira saltearnos
     # la primera linea, una variable de tipo diccionario y una lista
     # que sera la lista de materias

     primera = True;
     dictio = {}
     listadematerias = []

     # un bucle (loop para procesar todas las lineas del archivo)

     for lines in file:

        # si es la primera linea, no hacemos nada. Es el enacabezado.

        if primera:
           primera = False
        else:

           # a partir de la segunda, usamos como separados el ';' y
           # separamos la linea en cada parte que asignamos al array x

           x = lines.split(';')

           # x[0]=codigo, x[1]=materia, x[2]=calificatin, x[3]=fecha
           # si la calificacion es menor que 4 ( desaprobada )

           if (int ( x[2] ) < 4):

              # asignamos la materia con codigo y nombre al 
              # diccionario y el diccionario a una lista de materias
              # desaprobadas

              dictio["codigo"] = x[0]
              dictio["nombre"] = x[1]
              listadematerias.append(dictio)

  # la funcion devuelve como resultado la lista de diccionarios de materias

  return listadematerias


# programa principal, llamamnos a la funcion y asignamos el resultado 
# a una variable

listadesap = desaprobadas("11222333")

# imprimimos la variable

print(listadesap)
