
import csv
from os import listdir

ficheros=listdir("resultados")
setEntorno=set() #total de tags leidos por todas las configuraciones.

# cada repeticion se ha considerado como una nueva prueba, extrayendo un total de 8 resultados.
# El calculo del porcentaje es el siguiente: (testTags/totalTags)*100

for fichero in ficheros: #se guardan en setEntorno todas las lecturas de todas las configuraciones
    url='resultados/' + str(fichero)
    with open(url) as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            setEntorno.add(row[2]) #row[2] indica la posicion donde se guarda el id del tag.


y=float(len(setEntorno))
for fichero in ficheros:
    url='resultados/' + str(fichero)
    config=set() #set de tags de cada configuracion
    with open(url) as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            config.add(row[2])
    x=float(len(config))
    y=float(len(setEntorno))
    z=float(x/y) #(testTags/totalTags)
    print("Para el resultado "+ str(fichero)+ " el porcentaje de lecturas es: "+ str(round(z*100, 2))+ "%.\n" )
