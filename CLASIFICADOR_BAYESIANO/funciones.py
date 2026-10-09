from collections import defaultdict

def separarXY(datos):

    datos_y = datos.values.tolist()

    conteo_clases = {}

    for dato in datos_y:
        clase = dato[-1]
        if clase in conteo_clases:
            conteo_clases[clase] += 1
        else:
            conteo_clases[clase] = 1

    datos_x = (columna for columna in datos)

    return (datos_x, datos_y, conteo_clases)

def calcularPClase(datos_xy):

    total_datos_y = len(datos_xy[1])

    p_clase = {clase: cantidad / total_datos_y for clase, cantidad in datos_xy[2].items()}

    return p_clase

def contarPalabras(datos_y):
    
    conteo_palabras = defaultdict(lambda: defaultdict(int))

    vocabulario = set()

    for dato in datos_y:
        clase = dato[1]
        palabras = dato[0].lower().split(" ")
        for palabra in palabras:
            conteo_palabras[clase][palabra] += 1
            vocabulario.add(palabra)

    return (conteo_palabras, vocabulario)

def calcularProbabilidad(p_clase, nuevo_dato, conteo_palabras, vocabulario, total_palabras_clase):

    prob_datos = []

    veredictos = []

    ganador_datos = []

    for datos in nuevo_dato.values():

        for dato in datos:

            palabras = dato.lower().split(" ")
            
            probabilidades = {}

            for clase in p_clase:
                prob = p_clase[clase]
                for palabra in palabras:
                    prob *= (conteo_palabras[clase][palabra] + 1) / (total_palabras_clase[clase] + len(vocabulario))
                probabilidades[clase] = prob

            prob_datos.append(probabilidades)

            mayor_probabilidad = -1
            veredicto = None

            for clase in probabilidades:

                if probabilidades[clase] > mayor_probabilidad:

                    mayor_probabilidad = probabilidades[clase]
                    veredicto = clase

            veredictos.append(veredicto)

            maximo = max(probabilidades.values())
            ganadoras = []
            for clase, prob in probabilidades.items():
                if prob == maximo:
                    ganadoras.append(clase)

            ganador_datos.append(ganadoras)

    return (prob_datos, veredictos, ganador_datos)

