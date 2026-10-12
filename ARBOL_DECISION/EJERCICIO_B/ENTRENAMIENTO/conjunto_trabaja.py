import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

trabaja = datos[datos['trabaja/NoTrabaja'] == 'Si']
no_trabaja = datos[datos['trabaja/NoTrabaja'] == 'No']

total_conjunto = len(datos)

proporcion_trabaja = fn.calcularProporcion(trabaja, 'EstadoFinal', 'Continúa')
proporcion_no_trabaja = fn.calcularProporcion(no_trabaja, 'EstadoFinal', 'Continúa')

entropia_trabaja = fn.calcularEntropia(proporcion_trabaja, 'EstadoFinal', 'Continúa', trabaja)
entropia_no_trabaja = fn.calcularEntropia(proporcion_no_trabaja, 'EstadoFinal', 'Continúa', no_trabaja)

entropia_ponderada_trabaja = fn.calcularEntropiaPonderada(entropia_trabaja, len(trabaja), total_conjunto)
entropia_ponderada_no_trabaja = fn.calcularEntropiaPonderada(entropia_no_trabaja, len(no_trabaja), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_trabaja + entropia_ponderada_no_trabaja)

print(f'''
Entropia del conjunto "Trabaja": {entropia_trabaja} 

    Entropia ponderada del conjunto "Trabaja": {entropia_ponderada_trabaja}

Entropia del conjunto "No trabaja": {entropia_no_trabaja} 

    Entropia ponderada del conjunto "No trabaja": {entropia_ponderada_no_trabaja}

Ganancia de informacion: {ganancia}
''')