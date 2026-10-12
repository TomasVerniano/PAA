import pandas as pd
import funciones as fn

datos = pd.read_csv('ENTRENAMIENTO/TablaPrediccionAbandono-Entrenamiento.csv')

proporciones = fn.calcularProporcion(datos, 'EstadoFinal', 'Continúa')

entropia = fn.calcularEntropia(proporciones, 'EstadoFinal', 'Continúa', datos)

def main():
    print(f'''Proporciones:

    Continuan: {proporciones[0]}
    Abandonos: {proporciones[1]}

    Entropia del conjunto: {entropia}
    ''')

if __name__ == "__main__":
    main()