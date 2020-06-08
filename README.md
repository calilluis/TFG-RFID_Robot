# Diseño, análisis y construcción de la carga útil y mejora de un robot de inventario RFID basado en estigmergia.

En este repositorio se pueden encontrar todos los documentos anexos utilizados para el desarrollo del Trabajo de Final de Grado (TFG) sobre el desarrollo de un robot de Retail RFID. El Repositorio está pensado como un complemento de consulta al leer la Memoria, que se encuentra disponible en la raíz del repositorio, con nombre "Memoria.pdf".

Se pueden observar diversas carpetas:
  - **Caracterización Batería**
    - Apartado de la memoria relacionado: "2.2 Adaptación de la fuente de alimentación".
    - Contiene los archivos de datos de batería de las dos repeticiones que se llevan a cabo, así como el archivo "graficos_bateria.xlsx", que contiene los gráficos de batería extraídos de los datos obtenidos.
  - **Estudio de estilo**
    - Apartado de la memoria relacionado: "3.1 Diseño exterior (look and feel)".
    - Contiene un archivo .pdf que con todos los objetos que se evalúan para el estudio de estilo.
  - **Multimedia**
    - Contiene todos los archivos multimedia (no técnicos) que se han recopilado durante el trabajo (fotografías y videos).
   - **Presupuesto**
     - Apartado de la memoria relacionado: "2.5 Presupuesto".
     - Contiene un documento .xlsx que recoge los datos referentes al presupuesto.
   - **Pruebas de Entorno y Altura**
     - Apartado de la memoria relacionado: "2.1 Disposición y altura de las antenas".
     - Se observan dos carpetas, una para la prueba de entorno y la otra para la prueba de altura.
     - En el interior de ambas se pueden encontrar los scripts necesarios para procesar los resultados que se obtienen del proceso de inventario del robot.
     - Para ejecutar cualquier script de ambas pruebas:
       ```sh
       $ python <nombre_script.py>
       ```
      - También se recogen los resultados resumidos en tablas, después de ser procesados. Estos se encuentran disponibles en los archivos "tablas_analisis_entorno.xlsx" y "mapa_pruebaDobleFiltrado.xlsx" para la prueba de entorno, y "tablas_analisis_altura.xlsx" para la prueba de altura.
 - **Sistema de Notificaciones**
    - Apartado de la memoria relacionado: "3.2 Human-Robot Interface".
    - Se recogen los scripts que se integran en la estructura de ROS del sistema robótico. En concreto, se encuentran los scripts "script_node_BatteryManager.py" (nodo de control de batería) y "script_node_LedsController.py" (nodo de control de leds).
