import pandas as pd 
import math

def contarFilas(grupo, columna, valor):

    #Variables para contar cantidades
    a = 0
    b = 0

    #Contar las filas positivas
    for i in [fila for fila in grupo[columna] == valor]:
        if i == True:
            a += 1
    #Contar las filas negativas
        else:
            b += 1

    return (a, b)

def calcularProporcion(grupo, columna, valor):

    try:
        a_prop = contarFilas(grupo, columna, valor)[0] / (contarFilas(grupo, columna, valor)[0] + contarFilas(grupo, columna, valor)[1])
    except ZeroDivisionError:
         a_prop = 0
    
    try:
        b_prop = contarFilas(grupo, columna, valor)[1] / (contarFilas(grupo, columna, valor)[0] + contarFilas(grupo, columna, valor)[1])
    except ZeroDivisionError:
         b_prop = 0
         
    return (a_prop, b_prop)

def calcularEntropia(grupo_prop, columna, valor, grupo):

    if (contarFilas(grupo, columna, valor)[0] + contarFilas(grupo, columna, valor)[1]) == 0 or contarFilas(grupo, columna, valor)[0] == 0 or contarFilas(grupo, columna, valor)[1] == 0:
            return 0.0

    return - (grupo_prop[0] * math.log2(grupo_prop[0]) + grupo_prop[1] * math.log2(grupo_prop[1]))

def calcularEntropiaPonderada(grupo_entropia, cantidad, total):

        return ((cantidad / total) * grupo_entropia)