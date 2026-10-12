import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

poco = datos[datos['CantMateriasDesaprobadasPrimerCuatrimestre'] <= 2]
medio = datos[(datos['CantMateriasDesaprobadasPrimerCuatrimestre'] > 2) & (datos['CantMateriasDesaprobadasPrimerCuatrimestre'] <= 4)]
mucho = datos[datos['CantMateriasDesaprobadasPrimerCuatrimestre'] > 4]

total_conjunto = len(datos)

proporciones_poco = fn.calcularProporcion(poco, 'EstadoFinal', 'Continúa')
proporciones_medio = fn.calcularProporcion(medio, 'EstadoFinal', 'Continúa')
proporciones_mucho = fn.calcularProporcion(mucho, 'EstadoFinal', 'Continúa')

entropia_poco = fn.calcularEntropia(proporciones_poco, 'EstadoFinal', 'Continúa', poco)
entropia_medio = fn.calcularEntropia(proporciones_medio, 'EstadoFinal', 'Continúa', medio)
entropia_mucho = fn.calcularEntropia(proporciones_mucho, 'EstadoFinal', 'Continúa', mucho)

entropia_ponderada_poco = fn.calcularEntropiaPonderada(entropia_poco, len(poco), total_conjunto)
entropia_ponderada_medio = fn.calcularEntropiaPonderada(entropia_medio, len(medio), total_conjunto)
entropia_ponderada_mucho = fn.calcularEntropiaPonderada(entropia_mucho, len(mucho), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_poco + entropia_ponderada_medio + entropia_ponderada_mucho)

print(f'''
Entropia del conjunto "Poco": {entropia_poco} 

    Entropia ponderada del conjunto "Poco": {entropia_ponderada_poco}

Entropia del conjunto "Medio": {entropia_medio} 

    Entropia ponderada del conjunto "Medio": {entropia_ponderada_medio}

Entropia del conjunto "Mucho": {entropia_mucho} 

    Entropia ponderada del conjunto "Mucho": {entropia_ponderada_mucho}

Ganancia de informacion: {ganancia}
''')