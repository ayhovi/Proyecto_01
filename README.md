<p align="center">
  <img src="src/logo_henry.png" alt="Logo">
</p>

 
<h1 align="center"> PROYECTO INDIVIDUAL N°1 💥</h1>
<hr>

 
<h2 align="center">Machine Learning Operations (MLOps)</h2>
  <hr>
<h3 align="center">Sistema de recomendación de películas</h3>

## Resumen 📃 
<p align="justify">
Realizar un sistema de recomendaciones en una start-up que provee servicios de agregación de plataformas de streaming.

Para el cual tienes datos con 0 tratamiento ([Peliculas_Limpias.csv](https://github.com/ayhovi/Proyecto_01/blob/master/Datasets/Peliculas_Limpias.csv)), datos anidados, sin transformar, etc.

Por lo que es necesario realizar para este proyecto, ETL, API, EDA, deployment y un sistema de recomendaciones.

</p>

## Pasos del proyecto 📚
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

### 2. Análisis Exploratorio de Datos ( [ EDA ](https://github.com/BryanDarce01/PI_ML_OPS/blob/master/EDA.ipynb))

<p align="justify">
  En en este paso se exploran y visualizan los datos para tener un mejor entendimiento de la información que contiene el set de datos con el que se va a trabajar posteriormente.

</p>

###  3. Implementación de API´s ( [ Main ](https://github.com/BryanDarce01/PI_ML_OPS/blob/master/main.py))
<p align="justify">
  En el archivo main.py se desarrolló una interfaz utilizando las bibliotecas FastAPI. Esta interfaz permite a los usuarios interactuar con el modelo de Machine Learning al proporcionar los datos de entrada necesarios y obtener las predicciones correspondientes. 

  También se pueden realizar consultas y recibir respuestas en tiempo real a través de esta interfaz, lo que facilita la utilización y aplicación práctica del modelo desarrollado.

</p>

### 4. Desarrollo del Modelo de Machine Learning ( [ Main ](https://github.com/BryanDarce01/PI_ML_OPS/blob/master/main.py))
<p align="justify">
  Para el sistema de recomendación se implementó un modelo de Machine Learning utilizando el algoritmo de similitud de cosenos. 

  Este modelo ha sido entrenado utilizando los datos preprocesados y preparados. Una vez completado el entrenamiento, se procedió a realizar el despliegue de la aplicación utilizando la plataforma [RENDER ](https://darcemlops.onrender.com/docs). 

  El despliegue permite poner en funcionamiento el modelo y hacerlo accesible para su uso en la aplicación, brindando así la capacidad de realizar recomendaciones basadas en la similitud de cosenos de manera eficiente y efectiva.

# Stack Tecnológico 👨‍💻
<p align="justify">
  📊 **Scikit Learn**: Utilizado para vectorizar, tokenizar y calcular la similitud coseno.

  🐍**Python**: Lenguaje de programación principal utilizado en el desarrollo del proyecto.

  💻**Numpy**: Utilizado para realizar operaciones numéricas y manipulación de datos.

  🐼**Pandas**: Utilizado para la manipulación y análisis de datos estructurados.

  📈**Matplotlib**: Utilizado para la visualización de datos y generación de gráficos.

  📳**FastAPI**: Utilizado para crear la interfaz de la aplicación y procesar los parámetros de funciones.

  🌐**Render**: Plataforma utilizada para el despliegue del modelo y la aplicación.

</p>

# Recomendaciones ⚠️

- Al hacer las consultas usar la primera letra de cada palabra en mayusculas.
- No hacer uso de caracteres especiales.
- Para la función 1. Idioma, ingresar solamente las abreviaturas (Por ejemplo: 'english' = 'en' | 'español' = 'es' | 'francés' = 'fr' )

# Contacto 📱
[Bryan Darce](https://www.linkedin.com/in/bryan-darce/)