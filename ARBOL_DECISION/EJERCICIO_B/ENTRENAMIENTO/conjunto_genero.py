import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

masculino = datos[datos['genero'] == 'm']
femenino = datos[datos['genero'] == 'f']

total_conjunto = len(datos)

proporcion_masculino = fn.calcularProporcion(masculino, 'EstadoFinal', 'Continúa')
proporcion_femenino = fn.calcularProporcion(femenino, 'EstadoFinal', 'Continúa')

entropia_masculino = fn.calcularEntropia(proporcion_masculino, 'EstadoFinal', 'Continúa', masculino)
entropia_femenino = fn.calcularEntropia(proporcion_femenino, 'EstadoFinal', 'Continúa', femenino)

entropia_ponderada_masculino = fn.calcularEntropiaPonderada(entropia_masculino, len(masculino), total_conjunto)
entropia_ponderada_femenino = fn.calcularEntropiaPonderada(entropia_femenino, len(femenino), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_masculino + entropia_ponderada_femenino)

print(f'''
Entropia del conjunto "masculino": {entropia_masculino} 

    Entropia ponderada del conjunto "masculino": {entropia_ponderada_masculino}

Entropia del conjunto "femenino": {entropia_femenino} 

    Entropia ponderada del conjunto "femenino": {entropia_ponderada_femenino}

Ganancia de informacion: {ganancia}
''')