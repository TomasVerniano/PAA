import pandas as pd
import funciones_sklearn as fnsk

datos = pd.read_csv('noticias.csv')
datos_predict = pd.read_csv('noticia_nueva.csv')

datos_predict = datos_predict.values.tolist()

datos_predict_y = []

for lista in datos_predict:
    for item in lista:
        datos_predict_y.append(item)

# Paso 1: Separar caracteristicas y etiquetas
x_y = fnsk.separarCaracteristicasEtiquetas(datos)

# Paso 2 y 3: Dividir entrenamiento y prueba, y entrenar modelo
entrenamiento = fnsk.entrenarModelo(x_y[0], x_y[1])

# Paso 4: Evaluacion del modelo
evaluacion = fnsk.evaluarModelo(entrenamiento[0], entrenamiento[2], entrenamiento[4])

print(f"""Evaluacion del modelo:

Reporte de clasificacion: {evaluacion[1]}

Matriz de confusion: {evaluacion[2]}
""")

print("Clasificacion de nuevos datos: ")

# Paso 5: Clasificacion de nuevas noticias
prediccion = fnsk.predecir(datos_predict_y, entrenamiento[0], entrenamiento[5])
