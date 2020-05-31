
import csv
from os import listdir

ficheros=listdir("resultados")
setEntorno=list()

# cada repeticion se ha considerado como una nueva prueba, extrayendo un total de 8 resultados.
# El calculo del porcentaje es el siguiente: (testTags/totalTags)*100, pero solo se tienen en cuenta aquellos tags que se encuentren en el circuito

with open('baseground/total.csv') as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        setEntorno.append(row[2])

for fichero in ficheros:
    url='resultados/' + str(fichero)
    config=set()
    with open(url) as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            for row1 in setEntorno:
                if row[2] == row1:  #Solo se incluye el tag si forma parte del circuito
                    config.add(row[2])
    x=float(len(config))
    y=float(len(setEntorno))
    z=float(x/y)
    print("For result "+ str(fichero)+ " the average lectures are: "+ str(round(z*100, 2))+ "%.\n" )
