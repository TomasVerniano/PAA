import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

km5 = datos[datos['DistanciaDomicilioAlInstituto(Kms)'] <= 5]
km10 = datos[(datos['DistanciaDomicilioAlInstituto(Kms)'] > 5) & (datos['DistanciaDomicilioAlInstituto(Kms)'] <= 10)]
km15 = datos[(datos['DistanciaDomicilioAlInstituto(Kms)'] > 10) & (datos['DistanciaDomicilioAlInstituto(Kms)'] <= 15)]
lejos = datos[datos['DistanciaDomicilioAlInstituto(Kms)'] > 15]

total_conjunto = len(datos)

proporciones_km5 = fn.calcularProporcion(km5, 'EstadoFinal', 'Continúa')
proporciones_km10 = fn.calcularProporcion(km10, 'EstadoFinal', 'Continúa')
proporciones_km15 = fn.calcularProporcion(km5, 'EstadoFinal', 'Continúa')
proporciones_lejos = fn.calcularProporcion(lejos, 'EstadoFinal', 'Continúa')

entropia_km5 = fn.calcularEntropia(proporciones_km5, 'EstadoFinal', 'Continúa', km5)
entropia_km10 = fn.calcularEntropia(proporciones_km10, 'EstadoFinal', 'Continúa', km10)
entropia_km15 = fn.calcularEntropia(proporciones_km15, 'EstadoFinal', 'Continúa', lejos)
entropia_lejos = fn.calcularEntropia(proporciones_lejos, 'EstadoFinal', 'Continúa', lejos)

entropia_ponderada_km5 = fn.calcularEntropiaPonderada(entropia_km5, len(km5), total_conjunto)
entropia_ponderada_km10 = fn.calcularEntropiaPonderada(entropia_km10, len(km10), total_conjunto)
entropia_ponderada_km15 = fn.calcularEntropiaPonderada(entropia_km15, len(km15), total_conjunto)
entropia_ponderada_lejos = fn.calcularEntropiaPonderada(entropia_lejos, len(lejos), total_conjunto)

ganancia = entropia_original - (entropia_ponderada_km5 + entropia_ponderada_km10 + entropia_ponderada_km15 + entropia_ponderada_lejos)

print(f'''
Entropia del conjunto "km5": {entropia_km5} 

    Entropia ponderada del conjunto "km5": {entropia_ponderada_km5}

Entropia del conjunto "km10": {entropia_km10} 

    Entropia ponderada del conjunto "km10": {entropia_ponderada_km10}

Entropia del conjunto "km15": {entropia_km15} 

    Entropia ponderada del conjunto "km15": {entropia_ponderada_km15}

Entropia del conjunto "Lejos": {entropia_lejos} 

    Entropia ponderada del conjunto "Lejos": {entropia_ponderada_lejos}

Ganancia de informacion: {ganancia}
''')