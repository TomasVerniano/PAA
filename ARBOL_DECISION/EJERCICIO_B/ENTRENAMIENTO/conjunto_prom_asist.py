import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

bajo = datos[datos['AsistenciaPromedio(%)'] <= 25.0]
medio1 = datos[(datos['AsistenciaPromedio(%)'] > 25.0) & (datos['AsistenciaPromedio(%)'] <= 50.0)]
medio2 = datos[(datos['AsistenciaPromedio(%)'] > 50.0) & (datos['AsistenciaPromedio(%)'] <= 75.0)]
alto = datos[datos['AsistenciaPromedio(%)'] > 75.0]

total_conjunto = len(datos)

proporciones_bajo = fn.calcularProporcion(bajo, 'EstadoFinal', 'Continúa')
proporciones_medio1 = fn.calcularProporcion(medio1, 'EstadoFinal', 'Continúa')
proporciones_medio2 = fn.calcularProporcion(medio2, 'EstadoFinal', 'Continúa')
proporciones_alto = fn.calcularProporcion(alto, 'EstadoFinal', 'Continúa')

entropia_bajo = fn.calcularEntropia(proporciones_bajo, 'EstadoFinal', 'Continúa', bajo)
entropia_medio1 = fn.calcularEntropia(proporciones_medio1, 'EstadoFinal', 'Continúa', medio1)
entropia_medio2 = fn.calcularEntropia(proporciones_medio2, 'EstadoFinal', 'Continúa', medio2)
entropia_alto = fn.calcularEntropia(proporciones_alto, 'EstadoFinal', 'Continúa', alto)

entropia_ponderada_bajo = fn.calcularEntropiaPonderada(entropia_bajo, len(bajo), total_conjunto)
entropia_ponderada_medio1 = fn.calcularEntropiaPonderada(entropia_medio1, len(medio1), total_conjunto)
entropia_ponderada_medio2 = fn.calcularEntropiaPonderada(entropia_medio2, len(medio2), total_conjunto)
entropia_ponderada_alto = fn.calcularEntropiaPonderada(entropia_alto, len(alto), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_bajo + entropia_ponderada_medio1 + entropia_ponderada_medio2 + entropia_ponderada_alto)

print(f'''
Entropia del conjunto "bajo": {entropia_bajo} 

    Entropia ponderada del conjunto "bajo": {entropia_ponderada_bajo}

Entropia del conjunto "medio1": {entropia_medio1} 

    Entropia ponderada del conjunto "medio1": {entropia_ponderada_medio1}

Entropia del conjunto "medio2": {entropia_medio2} 

    Entropia ponderada del conjunto "medio2": {entropia_ponderada_medio2}

Entropia del conjunto "alto": {entropia_alto} 

    Entropia ponderada del conjunto "alto": {entropia_ponderada_alto}

Ganancia de informacion: {ganancia}
''')