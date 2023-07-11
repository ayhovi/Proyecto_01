<h1 align="center"> PROYECTO INDIVIDUAL N°1 💻</h1>

<p align="center">
  <img src="src/machi.png" alt="Logo">
</p>

 
<h2 align="center">Machine Learning Operations (MLOps)</h2>

<h3 align="center">Sistema de recomendación de películas</h3>

## Resumen 📃 
<p align="justify">
Realizar un sistema de recomendaciones en una start-up que provee servicios de agregación de plataformas de streaming.

Para el cual tienes datos con 0 tratamiento ([Peliculas_Limpias.csv](https://github.com/ayhovi/Proyecto_01/blob/master/Datasets/Peliculas_Limpias.csv)), datos anidados, sin transformar, etc.

Por lo que es necesario realizar para este proyecto, ETL, API, EDA, deployment y un sistema de recomendaciones.

Cumpliremos el Rol de <strong> Data Engnieer.

</p>

## PROCESO
### 1. Extracción, Transformación, Carga ( [ ETL ](https://github.com/BryanDarce01/PI_ML_OPS/blob/master/ETL_Peliculas.ipynb))
<p align="justify">

* Desanidar los campos que poseen diccionarios o lista de los mismos.
* Rellenar con el número 0 los valores nulos de los campos revenue, budget.
* Desanidar los campos que poseen diccionarios o lista de los mismos.
* Rellenar con el número 0 los valores nulos de los campos revenue, budget.
* De haber fechas, deberán tener el formato.AAAA-mm-dd
* Crear la columna release_year donde extraerán el año de la fecha de estreno.
* Crear la columna llamada return, dividiendo los campos.revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.
* Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.
* Exportar CSV final con todas las transformaciones.

</p>

### 2. Análisis Exploratorio de Datos ( [ EDA ](hhttps://github.com/ayhovi/Proyecto_01/blob/master/EDA.ipynb))

<p align="justify">
  Los datos ya estaban limpios, así que fue el momento de investigar las relaciones entre las variables de los conjuntos de datos. Busqué outliers o anomalías (que no necesariamente eran errores) ví si había algún patrón interesante que valiera la pena explorar en un análisis posterior. Las nubes de palabras proporcionaron una buena idea de qué palabras eran más frecuentes en los títulos, lo que podría ayudar al sistema de recomendación.

</p>

###  3. Implementación de API´s ( [ Main ](https://github.com/ayhovi/Proyecto_01/blob/master/main.py))
<p align="justify">
  Se desarrolló una interfaz en el archivo main.py utilizando la biblioteca FastAPI. Esta interfaz permite a los usuarios interactuar con el modelo de aprendizaje automático proporcionando los datos de entrada necesarios y obteniendo las predicciones correspondientes.

</p>

### 4. Desarrollo del Modelo de Machine Learning ( [ Main ](https://github.com/ayhovi/Proyecto_01/blob/master/main.py))
<p align="justify">
  Se implementó un modelo de aprendizaje automático utilizando el algoritmo de similitud coseno para el sistema de recomendación.
Este modelo fue entrenado utilizando datos preprocesados y preparados. Una vez completado el entrenamiento, se procedió a desplegar la aplicación utilizando la plataforma <a href="https://proyecto-02-y0jy.onrender.com/">RENDER</a>

El despliegue permite poner en funcionamiento el modelo y hacerlo accesible para su uso en la aplicación, proporcionando así la capacidad de realizar recomendaciones basadas en la similitud coseno de manera eficiente y efectiva.

# Tecnologias Aplicadas 💻
<p align="justify">
  📊 **Scikit Learn**: Utilizado para vectorizar, tokenizar y calcular la similitud coseno.

  🐍**Python**: Lenguaje de programación principal utilizado en el desarrollo del proyecto.

  💻**Numpy**: Utilizado para realizar operaciones numéricas y manipulación de datos.

  🐼**Pandas**: Utilizado para la manipulación y análisis de datos estructurados.

  📈**Matplotlib**: Utilizado para la visualización de datos y generación de gráficos.

  📳**FastAPI**: Utilizado para crear la interfaz de la aplicación y procesar los parámetros de funciones.

  🌐**Render**: Plataforma utilizada para el despliegue del modelo y la aplicación.

</p>

<p align="center">
  <img src="src/logo_henry.png" alt="Logo">
</p>