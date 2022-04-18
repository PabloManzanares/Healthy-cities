import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


st.write ("""
# 🌇🏃‍♀️ Mejores ciudades para vivir una vida saludable
""")

st.text("""🤔 ¿Alguna vez te has preguntado cual es la mejor ciudad para vivir? 

✔ Aquí se mostrarán algunos datos para poder obtener una solución""")

col1, col2 = st.columns(2)
with col1:
    imagen = Image.open("../images/portadaamsterdam.jpg")
    st.image(imagen, use_column_width=True)
with col2:
    imagen = Image.open("../images/portadaviena.jpg")
    st.image(imagen, use_column_width=True)


st.write(""" 
### 🗺🌍 Mapa interacctivo con distintos filtros de interés para la comparativa de ciudades""")

st.text("""🧐➡ En el siguiente mapa es posible realizar una comparación sencilla 
entre las distintas ciudades. 

De esta forma, se pueden modificar los filtros y, si se pincha encima de alguna 
de ellas, se desplegará una información básica.""")


HtmlFile = open("kepler.html", 'r', encoding='utf-8')

source_code = HtmlFile.read()

components.html(source_code,height=500)


st.write(""" 
### 📈📊 Gráficas comprativas de características comunes a las distintas ciudades.""")

col4, col5 = st.columns(2)
with col4:
    imagen = Image.open("../images/imagenparis.jpg")
    st.image(imagen, use_column_width=True)

with col5:
    st.text("""     Con los gráficos es sencillo comparar 
    características comunes para las distintas 
    ciudades, las cuales pueden repercutir de 
    manera significativa en su nivel de vida 
    saludable.""")


st.write(""" 
### 🤔 Comparativa esperanza de vida""")

st.text("""❕🧐 Como se puede observar en los dos gráficos que se muestran a continuación, 
no parece existir mucha relación entre los niveles de obesidad y esperanza de vida. 
Sorprendente... normalmente se tiende a pensar que sí es así.

Por otro lado, podemos pensar que la esperanza de vida responde a otros aspectos 
como, por ejemplo, la polución. 

En este segundo caso, si se aprecia una relación, pues en países 
con una gran contaminación, la esperanza de vida es mucho menor.""")

col6, col7 = st.columns(2)
with col6:
    imagen = Image.open("../images/Esperanza de vida dependiendo de los niveles de polución.png")
    st.image(imagen, use_column_width=True)

with col7:
    imagen = Image.open("../images/Esperanza de vida dependiendo de los niveles de obesidad.png")
    st.image(imagen, use_column_width=True)




st.write(""" 
### 🤔 Análisis de la influencia de las horas de sol en la vida saludable""")

st.text("""❕🧐 En este caso, las gráficas muestran que no parece existir una gran 
correlación entre el número de horas de sol y la felicidad de las personas. 

Además, estas horas de sol tampoco repercuten en los espacios al aire libre o las 
actividades realizadas en exteriores.

¿Podemos entonces decir que las horas de sol no afectan a la vida saludable en 
una ciudad?""")

col10, col11 = st.columns(2)
with col10:
    imagen = Image.open("../images/Felicidad de las personas dependiendo horas de sol y espacios al aire libre.png")
    st.image(imagen, use_column_width=True)

with col11:
    imagen = Image.open("../images/Número de actividades al aire libre dependiendo horas de sol.png")
    st.image(imagen, use_column_width=True)



