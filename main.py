from fastapi import FastAPI
import uvicorn
import pandas as pd
# from unidecode import unidecode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel


app = FastAPI(title = "Proyecto_01", description = "Proyecto_01")
df = pd.read_csv('Datasets/Peliculas_Limpias.csv')

#http://127.0.0.1:8000/


@app.get("/")
async def index ():
    output = "¡Bienvenido a la interfaz de consultas"
    return output

#Se desarrollan las consutlas que fueron solicitadas por el cliente:

#Consulta_1
#Se ingresa un idioma, retornando la cantidad de películas producidas en ese idioma.
@app.get('/peliculas_idioma/{Idioma}')
def peliculas_idioma(Idioma:str):
    sacar_idioma = df[df['Idioma'] == Idioma]
    total = len(sacar_idioma)
    return {'Respuesta': f"{total} peliculas se lanzaron en {Idioma}"}



#Consulta_2
#Se ingresa una pelicula, retornando la duracion y el año.
@app.get('/peliculas_dia/{Pelicula}')
def peliculas_duracion(Pelicula:str):
    peli = df[df['Titulo'] == Pelicula].iloc[0]
    duracion = peli['Duración']
    anio = peli['Año_Lanzamiento']
    return {'Respuesta': f"{Pelicula}. Duración: {duracion}. Año: {anio}"}

#Consulta_3
#Se ingresa la franquicia, La función retornara la cantidad de peliculas, ganancia total y promedio
@app.get('/franquicia/{Franquicia}')
def franquicia(Franquicia: str ): 
    valor_encontrado = df[df['Franquicia']==Franquicia]
    series = len(valor_encontrado)
    total = valor_encontrado['Ganancia'].sum()
    promedio = valor_encontrado['Ganancia'].mean()

    return {'Franquicia': Franquicia, 
            'Cantidad de Películas': series, 
            'Ganancias Totales': total, 
            'Promedio de las Ganancias': promedio}


#Consulta_4
#Se ingresa el país, retornando la cantidad de películas producidas en el mismo
@app.get('/peliculas_pais/{Pais}')
def peliculas_pais( Pais: str ):
    film_por_pais = df[df['Pais_de_Produccion'].str.contains(Pais,na=False,case=False)]
    cant = len(film_por_pais)
    
    return {'Respuesta':f"Se produjeron {cant} películas en {Pais}"}


#Consulta_5
#Se Ingresa la productora, retornando la ganancia total y la cantidad de películas que produjeron
@app.get('/productoras_exitosas/{Productora}')
def productoras_exitosas( Productora: str ):
    variable_productora=df[['Productora','Ganancia']].dropna()
    variable_productora['Productora']=variable_productora['Productora'].map(str.lower)
    variable_productora=variable_productora[variable_productora.Productora.str.contains(Productora.lower(), regex=False)]
    cantidad=variable_productora.shape[0]
    ganancia=variable_productora['Ganancia'].sum()
    return {'La productora':Productora, 
            'obtuvo ganancias de':ganancia, 
            'y las películas que hizo fueron':cantidad}


#CONSULTA_6
#Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.
@app.get('/get_director/{Director}')
def get_director(Director):
    resultado = []
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



# Consulta_7
# Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.
@app.get("/7. Recomendacion/{Titulo}")
def recomendacion(Titulo: str):
    df = pd.read_csv('Datasets/Peliculas_ML.csv')
    if Titulo not in df['Titulo'].values:
        return {'Respuesta': 'El título no existe en el DataFrame'}
    datos_reducidos = df.head(5000)
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
