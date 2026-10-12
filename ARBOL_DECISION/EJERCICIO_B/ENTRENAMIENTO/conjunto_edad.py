import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

joven = datos[datos['edad'] <= 20]
adulto1 = datos[(datos['edad'] > 20) & (datos['edad'] <= 40)]
adulto2 = datos[(datos['edad'] > 40) & (datos['edad'] <= 50)]
mayor = datos[datos['edad'] > 50]

total_conjunto = len(datos)

proporciones_joven = fn.calcularProporcion(joven, 'EstadoFinal', 'Continúa')
proporciones_adulto1 = fn.calcularProporcion(adulto1, 'EstadoFinal', 'Continúa')
proporciones_adulto2 = fn.calcularProporcion(adulto2, 'EstadoFinal', 'Continúa')
proporciones_mayor = fn.calcularProporcion(mayor, 'EstadoFinal', 'Continúa')

entropia_joven = fn.calcularEntropia(proporciones_joven, 'EstadoFinal', 'Continúa', joven)
entropia_adulto1 = fn.calcularEntropia(proporciones_adulto1, 'EstadoFinal', 'Continúa', adulto1)
entropia_adulto2 = fn.calcularEntropia(proporciones_adulto2, 'EstadoFinal', 'Continúa', adulto2)
entropia_mayor = fn.calcularEntropia(proporciones_mayor, 'EstadoFinal', 'Continúa', mayor)

entropia_ponderada_joven = fn.calcularEntropiaPonderada(entropia_joven, len(joven), total_conjunto)
entropia_ponderada_adulto1 = fn.calcularEntropiaPonderada(entropia_adulto1, len(adulto1), total_conjunto)
entropia_ponderada_adulto2 = fn.calcularEntropiaPonderada(entropia_adulto2, len(adulto2), total_conjunto)
entropia_ponderada_mayor = fn.calcularEntropiaPonderada(entropia_mayor, len(mayor), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_joven + entropia_ponderada_adulto1 + entropia_ponderada_adulto2 + entropia_ponderada_mayor)

print(f'''
Entropia del conjunto "Joven": {entropia_joven} 

    Entropia ponderada del conjunto "Joven": {entropia_ponderada_joven}

Entropia del conjunto "Adulto1": {entropia_adulto1} 

    Entropia ponderada del conjunto "Adulto1": {entropia_ponderada_adulto1}

Entropia del conjunto "Adulto2": {entropia_adulto2} 

    Entropia ponderada del conjunto "Adulto2": {entropia_ponderada_adulto2}

Entropia del conjunto "Mayor": {entropia_mayor} 

    Entropia ponderada del conjunto "Mayor": {entropia_ponderada_mayor}

Ganancia de informacion: {ganancia}
''')