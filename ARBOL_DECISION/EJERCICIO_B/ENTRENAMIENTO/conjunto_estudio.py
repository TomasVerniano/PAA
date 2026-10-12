import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

estudia = datos[datos['ActividadesExtracurriculares(Estudio)'] == 'Si']
no_estudia = datos[datos['ActividadesExtracurriculares(Estudio)'] == 'No']

total_conjunto = len(datos)

proporcion_estudia = fn.calcularProporcion(estudia, 'EstadoFinal', 'Continúa')
proporcion_no_estudia = fn.calcularProporcion(no_estudia, 'EstadoFinal', 'Continúa')

entropia_estudia = fn.calcularEntropia(proporcion_estudia, 'EstadoFinal', 'Continúa', estudia)
entropia_no_estudia = fn.calcularEntropia(proporcion_no_estudia, 'EstadoFinal', 'Continúa', no_estudia)

entropia_ponderada_estudia = fn.calcularEntropiaPonderada(entropia_estudia, len(estudia), total_conjunto)
entropia_ponderada_no_estudia = fn.calcularEntropiaPonderada(entropia_no_estudia, len(no_estudia), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_estudia + entropia_ponderada_no_estudia)

print(f'''
Entropia del conjunto "estudia": {entropia_estudia} 

    Entropia ponderada del conjunto "estudia": {entropia_ponderada_estudia}

Entropia del conjunto "No estudia": {entropia_no_estudia} 

    Entropia ponderada del conjunto "No estudia": {entropia_ponderada_no_estudia}

Ganancia de informacion: {ganancia}
''')