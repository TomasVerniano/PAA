import pandas as pd 
import funciones as fn

datos = pd.read_csv('noticias.csv')
datos_predict = pd.read_csv('noticia_nueva.csv')

datos_predict = datos_predict.to_dict(orient='list')

datos_xy = fn.separarXY(datos)

p_clase = fn.calcularPClase(datos_xy)

conteo_palabras = fn.contarPalabras(datos_xy[1])

total_palabras_clase = {clase: sum(palabras.values()) for clase, palabras in conteo_palabras[0].items()}

probabilidades = fn.calcularProbabilidad(p_clase, datos_predict, conteo_palabras[0], conteo_palabras[1], total_palabras_clase)

print(f"""
Paso 1: Calcular probabilidades previas - conteo_clases: {datos_xy[2]}
Paso 1: Calcular probabilidades previas - P_clase: {p_clase}

Paso 2: Conteo de palabras por clase - vocabulario: {conteo_palabras[1]}
Paso 2: Conteo de palabras por clase - conteo_palabras: {conteo_palabras[0]}

Paso 3: Calcular probabilidades con suavizado de Laplace: {probabilidades[0]}

Probabilidades calculadas para el/los dato/s nuevo/s: 
{probabilidades[0]}

El/los nuevo/s dato/s se clasifica/n como: {probabilidades[1]}

Ganador/es: {probabilidades[2]}
""")