# Prueba de entorno

**1 - Porcentaje de lecturas en bruto:**  
--script_entorno_1-lecturasEnBruto.py--  
En el script, se guardan todos los tags de las 4 configuraciones × 2 repeticiones en una misma variable (setEntorno) procesando los 8 archivos disponibles usando la librería ‘csv’ de Python. A continuación, se procesan las lecturas de cada una y se guardan en una variable temporal (config). Finalmente se muestra el resultado en porcentaje, (#tags de cada configuración / #setEntorno) × 100.    
**2 - Porcentaje de lecturas filtradas:**  
--script_entorno_2-filtroLecturas.py--  
En el script de esta prueba, en la variable setEntorno se guardan todos los tags que están en el circuito (baseground). El siguiente paso es idéntico al Script 1: Se procesan las lecturas de cada fichero y se muestra el porcentaje (#tags de cada configuración / #setEntorno) × 100.    
**2.1 - Filtro doble:**  
--script_entorno_2.1-filtroDoble.py--  
El script es similar al anterior, pero en este caso se reprocesa el set de entorno (setEntorno) para eliminar aquellos tags que no hayan sido leídos por ninguna configuración. A continuación, se sigue el mismo proceso que en el Script 2: Se descartan los tags que hayan sido leídos, pero no formen parte del circuito, y se muestra el resultado (#tags de cada configuración / #setEntorno) × 100.    
**2.2 - Porcentajes por antena:**  
--script_entorno_2.2-porAntena.py--  
El script se incorpora en este caso el porcentaje leído por cada puerto del reader en cada uno de los 8 ficheros.    
**3 - Mapa de doble filtrado:**  
-- script_entorno_3-mapaDobleFiltro.py--  
En el script se crea una lista de sets (variable listofsets), donde cada posición de la lista es un frozen set (set inmutable) que contiene los tags leídos por una prueba de las 8 (por tanto, el tamaño de la lista es de 8 posiciones). A continuación, se crea un doble bucle, que carga los archivos de una carpeta donde cada archivo hace referencia a un bloque de tags del circuito. Finalmente se printa, para cada bloque, los promedios de las 2 iteraciones de cada configuración.
