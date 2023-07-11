from fastapi import FastAPI
import uvicorn
import pandas as pd
# from unidecode import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel


app = FastAPI()
df = pd.read_csv('Datasets/Peliculas_Limpias.csv')

#http://127.0.0.1:8000/


'''
@app.get('/prueba')
def prueba():
    return {'Mensaje': 'Hola'}
'''


# 1. 
@app.get('/1. Idioma/{Idioma}')
def peliculas_idioma(Idioma:str):
    '''Se ingresa un idioma con su abreviatura y devuelve la cantidad de películas producidas en ese idioma.'''
    sacar_idioma = df[df['Idioma'] == Idioma]
    total = len(sacar_idioma)
    return {'Respuesta': f"{total} peliculas se lanzaron en {Idioma}"}



# 2.
@app.get('/2. Duracion/{Pelicula}')
def peliculas_duracion(Pelicula:str):
    '''Se ingresa una pelicula. Debe devolver la duracion y el año.'''
    peli = df[df['Titulo'] == Pelicula].iloc[0]
    duracion = peli['Duración']
    anio = peli['Año_Lanzamiento']
    return {'Respuesta': f"{Pelicula}. Duración: {duracion}. Año: {anio}"}


# 3.
@app.get('/3. Franquicia/{Franquicia}')
def franquicia(Franquicia: str ): 
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio.'''
    valor_encontrado = df[df['Franquicia']==Franquicia]
    series = len(valor_encontrado)
    total = valor_encontrado['Ganancia'].sum()
    promedio = valor_encontrado['Ganancia'].mean()

    return {'Franquicia': Franquicia, 
            'Cantidad de Películas': series, 
            'Ganancias Totales': total, 
            'Promedio de las Ganancias': promedio}


# 4.
@app.get('/4. Pais/{Pais}')
def peliculas_pais( Pais: str ):
    '''Se ingresa un país, retornando la cantidad de peliculas producidas en el mismo.'''
    film_por_pais = df[df['Pais_de_Produccion'].str.contains(Pais,na=False,case=False)]
    cant = len(film_por_pais)
    
    return {'Respuesta':f"Se produjeron {cant} películas en {Pais}"}


# 5. 
@app.get('/5. Productora/{Productora}')
def productoras_exitosas( Productora: str ):
    '''Se ingresa la productora, entregandote el revenue total y la cantidad de peliculas que realizo.'''
    variable_productora=df[['Productora','Ganancia']].dropna()
    variable_productora['Productora']=variable_productora['Productora'].map(str.lower)
    variable_productora=variable_productora[variable_productora.Productora.str.contains(Productora.lower(), regex=False)]
    cantidad=variable_productora.shape[0]
    ganancia=variable_productora['Ganancia'].sum()
    return {'La productora':Productora, 
            'obtuvo ganancias de':ganancia, 
            'y las películas que hizo fueron':cantidad}


# 6. Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver 
# el éxito del mismo medido a través del retorno. 
# Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, 
# retorno individual, costo y ganancia de la misma, en formato lista.

@app.get('/6. Director/{Director}')
def get_director(Director):
    '''Se ingresa el nombre de un director y devuelve la información de cada película en la que trabajó'''
    resultado = []

    # En el ciclo For, usé "_" porque no es necesario trabajar con el índice
    # Esto evita la necesidad de trabajar con una tupla en cada iteración 
    # y podemos acceder directamente a los valores de la serie utilizando row['Director'], row['Titulo'],
    for _, row in df.iterrows():
        director = row['Director']
        if isinstance(director, str) and Director.lower() == director.lower():
            titulo = row['Titulo']
            fecha_lanzamiento = pd.to_datetime(row['Fecha_Lanzamiento']).date()
            ganancia = round(row['Ganancia'], 9)
            presupuesto = int(row['Presupuesto'])
            ingresos = int(row['Ingresos'])
            
            pelicula = {
                'Titulo': titulo,
                'Fecha de lanzamiento': fecha_lanzamiento,
                'Ganancia': ganancia,
                'Presupuesto': presupuesto,
                'Ingresos Totales': ingresos
            }
            
            resultado.append(pelicula)
    
    if not resultado:
        resultado = "No se encontró al director especificado."

    return resultado



# 7. Sistema de Recomendación

@app.get("/7. Recomendacion/{Titulo}")
def recomendacion(Titulo: str):
    ''' Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.'''
    df = pd.read_csv('Datasets/Peliculas_ML.csv')

    # Verificar si el título existe en el DataFrame original
    if Titulo not in df['Titulo'].values:
        return {'Respuesta': 'El título no existe en el DataFrame'}

    # Reducción del tamaño del DataFrame con el título incluido
    datos_reducidos = df.head(5000)

    # Verificar nuevamente si el título existe en la muestra reducida
    if Titulo not in datos_reducidos['Titulo'].values:
        return {'Respuesta': 'El título no existe en la muestra reducida'}

    tfidf = TfidfVectorizer(stop_words='english')
    datos_reducidos['Resumen'] = datos_reducidos['Resumen'].fillna('')

    tdfidf_matrix = tfidf.fit_transform(datos_reducidos['Resumen'])
    cosenoSimilaridad = linear_kernel(tdfidf_matrix, tdfidf_matrix)

    indices = datos_reducidos[datos_reducidos['Titulo'] == Titulo].index[0]

    peliculas_similares = list(enumerate(cosenoSimilaridad[indices]))
    peliculas_ordenadas = sorted(peliculas_similares, key=lambda tupla: tupla[1], reverse=True)
    extraer_indices = [i for i, _ in peliculas_ordenadas[1:6]]
    respuesta = datos_reducidos['Titulo'].iloc[extraer_indices].values.tolist()

    return respuesta
