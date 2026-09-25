import pandas as pd 
import math
import funciones as fn

datos = pd.read_csv("telecom.csv", sep=" ")

def calcularOriginal(datos):

    proporciones = fn.calcularProporcion(datos, 'Aceptó_oferta', 'Sí')

    entropia = fn.calcularEntropia(proporciones, 'Aceptó_oferta', 'Sí', datos)
    
    return entropia

def calcularGananciaEdad(datos, entropia_original):

    joven = datos[datos['Edad'] <= 30]
    adulto = datos[(datos['Edad'] > 30) & (datos['Edad'] <= 50)]
    mayor = datos[datos['Edad'] > 50]

    total = len(datos['ID'])

    proporciones_joven = fn.calcularProporcion(joven, 'Aceptó_oferta', 'Sí')
    proporciones_adulto = fn.calcularProporcion(adulto, 'Aceptó_oferta', 'Sí')
    proporciones_mayor = fn.calcularProporcion(mayor, 'Aceptó_oferta', 'Sí')

    entropia_joven = fn.calcularEntropia(proporciones_joven, 'Aceptó_oferta', 'Sí', joven)
    entropia_adulto = fn.calcularEntropia(proporciones_adulto, 'Aceptó_oferta', 'Sí', adulto)
    entropia_mayor = fn.calcularEntropia(proporciones_mayor, 'Aceptó_oferta', 'Sí', mayor)

    ganancia = entropia_original - (fn.calcularEntropiaPonderada(entropia_joven, len(joven), total) + \
                                    fn.calcularEntropiaPonderada(entropia_adulto, len(adulto), total) + \
                                    fn.calcularEntropiaPonderada(entropia_mayor, len(mayor), total)
                                    )

    return ganancia

def calcularGananciaLinea(datos, entropia_original):

    tiene = datos[datos['Tiene_línea_fija'] == 'Sí']
    no_tiene = datos[datos['Tiene_línea_fija'] == 'No']

    total = len(datos['ID'])

    proporciones_tiene = fn.calcularProporcion(tiene, 'Aceptó_oferta', 'Sí')
    proporciones_no_tiene = fn.calcularProporcion(no_tiene, 'Aceptó_oferta', 'Sí')

    entropia_tiene = fn.calcularEntropia(proporciones_tiene, 'Aceptó_oferta', 'Sí', tiene)
    entropia_no_tiene = fn.calcularEntropia(proporciones_no_tiene, 'Aceptó_oferta', 'Sí', no_tiene)

    ganancia = entropia_original - (fn.calcularEntropiaPonderada(entropia_tiene, len(tiene), total) + \
                                    fn.calcularEntropiaPonderada(entropia_no_tiene, len(no_tiene), total)
                                    )

    return ganancia

def calcularGananciaDatos(datos, entropia_original):

    bajo = datos[datos['Uso_de_datos'] <= 3.0]
    medio = datos[(datos['Uso_de_datos'] > 3.0) & (datos['Uso_de_datos'] <= 6.0)]
    alto = datos[datos['Uso_de_datos'] > 6.0]

    total = len(datos['ID'])

    proporciones_bajo = fn.calcularProporcion(bajo, 'Aceptó_oferta', 'Sí')
    proporciones_medio = fn.calcularProporcion(medio, 'Aceptó_oferta', 'Sí')
    proporciones_alto = fn.calcularProporcion(alto, 'Aceptó_oferta', 'Sí')

    entropia_bajo = fn.calcularEntropia(proporciones_bajo, 'Aceptó_oferta', 'Sí', bajo)
    entropia_medio = fn.calcularEntropia(proporciones_medio, 'Aceptó_oferta', 'Sí', medio)
    entropia_alto = fn.calcularEntropia(proporciones_alto, 'Aceptó_oferta', 'Sí', alto)

    ganancia = entropia_original - (fn.calcularEntropiaPonderada(entropia_bajo, len(bajo), total) + \
                                    fn.calcularEntropiaPonderada(entropia_medio, len(medio), total) + \
                                    fn.calcularEntropiaPonderada(entropia_alto, len(alto), total)
                                    )

    return ganancia

entropia_original = calcularOriginal(datos)

print("Entropia del conjunto original: \n", entropia_original)

print("Punto A. 2. a: Ganancia por edad \n", calcularGananciaEdad(datos, entropia_original))

print("Punto A. 2. b: Ganancia por Telefono de Linea \n", calcularGananciaLinea(datos, entropia_original))

print("Punto A. 2. c: Ganancia por Uso de Datos \n", calcularGananciaDatos(datos, entropia_original))
