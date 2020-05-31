
import csv
from os import listdir

setEntorno=list()
setDatos=set()
resultados=listdir("resultados")

for file in resultados: #coger todas las lecturas de todas las configuraciones
    url='resultados/' + str(file)
    with open(url) as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            setDatos.add(row[2])

with open('baseground/total.csv') as data: #Solo se usaran los tags del circuito que hayan sido leidos por al menos 1 configuracion.
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        for row1 in setDatos:
            if row[2] == row1:
                setEntorno.append(row[2])


# cada repeticion se ha considerado como una nueva prueba, extrayendo un total de 8 resultados.
# El calculo del porcentaje es el siguiente: (testTags/totalTags)*100, pero solo se tienen en cuenta aquellos tags que se encuentren en el circuito y hayan sido leidos por al menos 1 configuracion.

for file in resultados:
    url='resultados/' + str(file)
    config=set()
    with open(url) as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            for row1 in setEntorno:
                if row[2] == row1:  #Solo se incluye el tag si forma parte del circuito
                    config.add(row1)
        x=float(len(config))
        y=float(len(setEntorno))
        z=float(x/y)
        print("For result "+ str(file)+ " the average lectures are: "+ str(round(z*100, 2))+ "%.\n" )
