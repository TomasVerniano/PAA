import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

bajo = datos[datos['PromedioPrimerCuatrimestre'] < 4.00]
medio = datos[(datos['PromedioPrimerCuatrimestre'] >= 4.00) & (datos['PromedioPrimerCuatrimestre'] < 7.00)]
alto = datos[datos['PromedioPrimerCuatrimestre'] >= 7.00]

total_conjunto = len(datos)

proporciones_bajo = fn.calcularProporcion(bajo, 'EstadoFinal', 'Continúa')
proporciones_medio = fn.calcularProporcion(medio, 'EstadoFinal', 'Continúa')
proporciones_alto = fn.calcularProporcion(alto, 'EstadoFinal', 'Continúa')

entropia_bajo = fn.calcularEntropia(proporciones_bajo, 'EstadoFinal', 'Continúa', bajo)
entropia_medio = fn.calcularEntropia(proporciones_medio, 'EstadoFinal', 'Continúa', medio)
entropia_alto = fn.calcularEntropia(proporciones_alto, 'EstadoFinal', 'Continúa', alto)

entropia_ponderada_bajo = fn.calcularEntropiaPonderada(entropia_bajo, len(bajo), total_conjunto)
entropia_ponderada_medio = fn.calcularEntropiaPonderada(entropia_medio, len(medio), total_conjunto)
entropia_ponderada_alto = fn.calcularEntropiaPonderada(entropia_alto, len(alto), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_bajo + entropia_ponderada_medio + entropia_ponderada_alto)

print(f'''
Entropia del conjunto "Bajo": {entropia_bajo} 

    Entropia ponderada del conjunto "Bajo": {entropia_ponderada_bajo}

Entropia del conjunto "Medio": {entropia_medio} 

    Entropia ponderada del conjunto "Medio": {entropia_ponderada_medio}

Entropia del conjunto "Alto": {entropia_alto} 

    Entropia ponderada del conjunto "Alto": {entropia_ponderada_alto}

Ganancia de informacion: {ganancia}
''')