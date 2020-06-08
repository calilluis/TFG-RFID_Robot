import csv
from os import listdir


config=set()
listofsets=list()
names=["2inclinadas", "original", "cuadrado", "rombo"]
resultados=listdir("resultados") #El orden es: inc1,2 act1,2 cuad1,2 rombo1,2
#load info from the data results
for resultat in resultados:
    urlr='resultados/' + str(resultat)
    config=set();
    with open(urlr) as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            config.add(row[2])
        listofsets.append(frozenset(config))
#------------------------------------------------------

#load info from baseground
files=listdir("baseground_files")
i=0
for file in files:
    listofresults=list()
    print("RESULTADOS DEL BLOQUE "+ str(file))
    for set in listofsets:
        result=0
        total=0
        url='baseground_files/' + str(file)
        with open(url) as data:
            reader = csv.reader(data, delimiter=',')
            for row in reader:
                total=total+1;
                for row2 in set:
                    if row[2] == row2:
                        result=result+1
            x=float(result)
            y=float(total)
            z=float(x/y)
            listofresults.append(z)
    i+=1
    a=0
    b=0;
    while a<len(listofresults):

        print("for "+ names[b]+ " we have a medium of "+ str(round(float((float(listofresults[a])+float(listofresults[a+1]))/2)*100,2))+ "%")
        a+=2
        b+=1
    print("\n")
