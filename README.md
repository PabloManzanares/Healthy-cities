# Proyecto_Pablo_Manzanares

![portada](https://es.wikipedia.org/wiki/Ciudad_global#/media/Archivo:Skyscrapers_of_Shinjuku_2009_January.jpg)

# Objetivo.

🌇🏃‍♀️ El objetivo del proyecto es un análisis comparativo sobre el nivel de vida saludable en distintas ciudades del mundo. De esta forma, se pretenden estudiar los siguientes puntos:

1️⃣ Obtención de un csv con la distinta información característica de cada ciudad, en la que se incluyan datos de interés para determinar el nivel de vida saludable. Además, también deberá incluir la localización de cada una de las ciudades.

2️⃣ Creación de un mapa iteractivo con el que se pueda realizar de manera fácil y rápida un estudio comparativo de las distintas ciudades a partir de los distintos parámetros obtenidos con anterioridad.

3️⃣ Producción de gráficos que permitan visualizar y comparar, de manera sencilla, los datos específicos de cada ciudad.

4️⃣ Presentación del conjunto de datos recopilados a partir de un data app.

❗ El csv empleado inicialmente contendrá información sobre: las horas de sol, la contaminación, la esperanza de vida, la obesidad media, las actividades realizadas en espacios exteriores, los costes de una botella de agua o un mes de gimnasio, el nivel de felicidad medio de las personas o las horas medias trabajadas.


# Obtención resultados.

**Regex:** permite la limpieza del csv, eliminando los datos innecesarios y que pueden suponer un problema posterior para el análisis de los mismos.


**Geopy:** es el método empleado para lograr la geolocalización de las distintas ciudades, aspecto necesario para la posterior creación de un mapa.


**Kepler:** permite la creación de un mapa donde situar cada una de las ciudades estudiadas y favorece su análisis gracias a las siguientes herramientas:

1️⃣ Información del ranking que ocupa la ciudad y el nivel medio de felicidad al pinchar en cada una de las ciudades sobre el mapa.

2️⃣ Filtros para su diferenciación, permitiendo distinguirlas según su nivel de horas de sol, esperanza de vida, horas trabajadas de media al año o el nivel medio de felicidad de sus habitantes.

**SQL:** es el programa empleado para realizar un análisis de datos relacionales, es decir, relacionados entre sí. Para ello, se divide el csv inicial en tres: uno con características de las ciudades, otro con los costes asociados a vivir en ella y, por último, otro sobre los datos de las personas que viven en ella.

De este modo, es posible realizar un análisis relacional a partir de estos tres csv por separado.


**Gráficas:** fueron empleadas para realizar un análisis de las obras de los distintos artistas, comprobando proncipalmente dos situaciones:

1️⃣ Mayoritariamente cuantas obras pintaron los autores, es decir, cual es, por lo general, el número de obras pintadas por los autores. 

2️⃣ Género con mayor número de obras pintadas.


**Streamlit:** sirve como medio para la creación de un data app donde exponer los datos y análisis realizado de manera ordenada y vistosa.


# Estructura del proyecto.

1️⃣ **notebook:** contiene los jupyter de trabajo, el streamlit y el modelo de SQL.

*Limpieza csv:* limpieza del csv inicial.

*Obtención localización:* obtención de la localización (latitud y longitud) de cada una de las ciudades.

*SQL:* conexión de nuestros datos con SQL, para la posible realización de un análisis relacional.
    
*Análisis ciudades:* gráficas con la comparativa sencilla y visual de los distintos datos de interes de las respectivas ciudades. 

*SQL-rankciudades:* modelo de SQL realizado para el análisis de nuestros datos, en el que se pueden apreciar las distintas conexiones entre cada una de las tablas.

*streamlit:* código realizado para la creación del data app que permita la visualización clara de los datos y conclusiones obtenidas.

*kepler.html:* mapa kepler con las características de las distintas ciudades y una comparativa simple.


2️⃣ **src:** funciones empleadas en el proyecto.

*funcioneslocalizacion.py:* funciones empleadas para la obtención de la latitud y longitud de cada ciudad.


3️⃣ **images:** imágenes de las gráficas obtenidas y de distintas ciudades.


4️⃣ **data:** distintos csv empleados y creados en el proyecto.

*vida_ciudades.csv:* csv inicial a partir del cual se realiza el proyecto.

*actividades_ciudad.csv:* contiene información sobre las actividades al aire libre y los costes de una botella de agua o la cuota de un gimnasio mensualmente para las distintas ciudades.

*calidad_personas.csv:* abarca los aspectos específicos de las personas que viven en las respetivas ciudades, como los niveles de obesidad, la esperanza de vida, las horas trabajadas anualmente o el nivel de felicidad medio.

*caracteristica_ciudad.csv:* csv con las horas de sol, la polución o los distintos lugares al aire libre disponibles para cada una de las ciudades.

*ciudades.csv*: csv que recoge el conjunto de los tres últimos csv descritos en uno solo.

*coord_ciudades.csv:* contiene la información de la localización, con su respectiva longitud y latitud.

*calidad_ciudades.csv:* csv final, con toda la información y la localización de las respectivas ciudades.


# Librerías.

[pandas] (https://pandas.pydata.org/)

[numpy] (https://numpy.org/)

[regex] (https://docs.python.org/3/library/re.html)

[request] (https://docs.python-requests.org/en/latest/)

[sys] (https://docs.python.org/3/library/sys.html)

[sqlalchemy] (https://www.sqlalchemy.org/)

[geopy] (https://geopy.readthedocs.io/en/stable/)

[streamlit] (https://streamlit.io/)

[seaborn] (https://seaborn.pydata.org/)

[matplotlib] (https://matplotlib.org/)
