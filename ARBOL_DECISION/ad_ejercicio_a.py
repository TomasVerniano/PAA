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

    a_prop = contarFilas(grupo, columna, valor)[0] / (contarFilas(grupo, columna, valor)[0] + contarFilas(grupo, columna, valor)[1])

    b_prop = contarFilas(grupo, columna, valor)[1] / (contarFilas(grupo, columna, valor)[0] + contarFilas(grupo, columna, valor)[1])

    return (a_prop, b_prop)

def calcularEntropia(grupo_prop, clave1, clave2, columna, valor, grupo):

    if (contarFilas(grupo, columna, valor)[0] + contarFilas(grupo, columna, valor)[1]) == 0 or contarFilas(grupo, columna, valor)[0] == 0 or contarFilas(grupo, columna, valor)[1] == 0:
            return 0.0

    return (- (grupo_prop[clave1] * math.log2(grupo_prop[clave1]) + grupo_prop[clave2] * math.log2(grupo_prop[clave2])))

def calcularEntropiaPonderada(grupo_entropia, grupo, total):

        return ((len(grupo['ID']) / total) * grupo_entropia)

def calcularOriginal():

    #Cargar los datos
    datos = pd.read_csv("telecom.csv", sep=" ")

    #Donde guardamos las proporciones
    conjunto_original_prop = {
        "acepto_prop" : 0,
        "no_acepto_prop" : 0
    }

    #Variables para contar cantidades
    aceptados = 0
    no_aceptados = 0

    #Contar las filas donde se acepto la oferta
    for i in [fila for fila in datos['Aceptó_oferta'] == 'Sí']:
        if i == True:
            aceptados += 1
    #Contar las filas donde no se acepto la oferta
        else:
            no_aceptados += 1

    #Calcular y guardar proporciones 
    conjunto_original_prop['acepto_prop'] = aceptados / (aceptados + no_aceptados)
    conjunto_original_prop['no_acepto_prop'] = no_aceptados / (aceptados + no_aceptados)

    #Calcular la entropia
    entropy = - (conjunto_original_prop['acepto_prop'] * math.log2(conjunto_original_prop['acepto_prop']) + \
                 conjunto_original_prop['no_acepto_prop'] * math.log2(conjunto_original_prop['no_acepto_prop']))

    return entropy

def calcularGananciaEdad(clave1, clave2, columna, valor):

    #Cargar los datos
    datos = pd.read_csv("telecom.csv", sep=" ")

    jovenes = datos[datos['Edad'] <= 30]
    adultos = datos[(datos['Edad'] > 30) & (datos['Edad'] <= 50)]
    mayores = datos[datos['Edad'] > 50]

    total = len(jovenes['ID']) + len(adultos['ID']) + len(mayores['ID'])

    jovenes_prop = {
        "acepto_prop" : calcularProporcion(jovenes, columna, valor)[0],
        "no_acepto_prop" : calcularProporcion(jovenes, columna, valor)[1]
    }

    adultos_prop = {
        "acepto_prop" : calcularProporcion(adultos, columna, valor)[0],
        "no_acepto_prop" : calcularProporcion(adultos, columna, valor)[1]
    }

    mayores_prop = {
        "acepto_prop" : calcularProporcion(mayores, columna, valor)[0],
        "no_acepto_prop" : calcularProporcion(mayores, columna, valor)[1]
    }

    jovenes_entropia = calcularEntropia(jovenes_prop, clave1, clave2, columna, valor, jovenes)
    adultos_entropia = calcularEntropia(adultos_prop, clave1, clave2, columna, valor, adultos)
    mayores_entropia = calcularEntropia(mayores_prop, clave1, clave2, columna, valor, mayores)

    ganancia_edad = calcularOriginal() - (calcularEntropiaPonderada(jovenes_entropia, jovenes, total) + \
                                          calcularEntropiaPonderada(adultos_entropia, adultos, total) + \
                                          calcularEntropiaPonderada(mayores_entropia, mayores, total) )

    return (ganancia_edad)

def calcularGananciaLinea(clave1, clave2, columna, valor1, valor2):

    #Cargar los datos
    datos = pd.read_csv("telecom.csv", sep=" ")

    tiene = datos[datos[columna] == valor1]
    no_tiene = datos[datos[columna] == valor2]

    total = len(tiene['ID']) + len(no_tiene['ID'])

    linea_prop = {
        "tiene_prop" : calcularProporcion(tiene, columna, valor1)[0],
        "no_tiene_prop" : calcularProporcion(tiene, columna, valor1)[1]
    }

    tiene_entropia = calcularEntropia(linea_prop, clave1, clave2, columna, valor1, tiene)
    no_tiene_entropia = calcularEntropia(linea_prop, clave1, clave2, columna, valor1, no_tiene)

    ganancia_linea = calcularOriginal() - (calcularEntropiaPonderada(tiene_entropia, tiene, total) + \
                                         calcularEntropiaPonderada(no_tiene_entropia, no_tiene, total))

    return (ganancia_linea)

def calcularGananciaDatos(clave1, clave2, columna, valor):

    datos = pd.read_csv("telecom.csv", sep=" ")

    bajo = datos[datos['Uso_de_datos'] <= 3.0]
    medio = datos[(datos['Uso_de_datos'] > 3.0) & (datos['Uso_de_datos'] <= 6.0)]
    alto = datos[datos['Uso_de_datos'] > 6.0]

    total = len(bajo['ID']) + len(medio['ID']) + len(alto['ID'])

    bajo_prop = {
        "acepto_prop" : calcularProporcion(bajo, columna, valor)[0],
        "no_acepto_prop" : calcularProporcion(bajo, columna, valor)[1]
    }

    medio_prop = {
        "acepto_prop" : calcularProporcion(medio, columna, valor)[0],
        "no_acepto_prop" : calcularProporcion(medio, columna, valor)[1]
    }

    alto_prop = {
        "acepto_prop" : calcularProporcion(alto, columna, valor)[0],
        "no_acepto_prop" : calcularProporcion(alto, columna, valor)[1]         
    }

    bajo_entropia = calcularEntropia(bajo_prop, clave1, clave2, columna, valor, bajo)
    medio_entropia = calcularEntropia(medio_prop, clave1, clave2, columna, valor, medio)
    alto_entropia = calcularEntropia(alto_prop, clave1, clave2, columna, valor, alto)

    ganancia_datos = calcularOriginal() - (calcularEntropiaPonderada(bajo_entropia, bajo, total) + \
                                           calcularEntropiaPonderada(medio_entropia, medio, total) + \
                                           calcularEntropiaPonderada(alto_entropia, alto, total))

    return (ganancia_datos)

print("Punto A. 2. a: Ganancia por edad \n", calcularGananciaEdad('acepto_prop', 'no_acepto_prop', 'Aceptó_oferta', 'Sí'))

print("Punto A. 2. b: Ganancia por Telefono de Linea \n", calcularGananciaLinea('tiene_prop', 'no_tiene_prop', 'Tiene_línea_fija', 'Sí', 'No'))

print("Punto A. 2. c: Ganancia por Uso de Datos \n", calcularGananciaDatos('acepto_prop', 'no_acepto_prop', 'Uso_de_datos', 'Sí'))
