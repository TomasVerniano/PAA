import funciones as fn
from conjunto_original import entropia, datos

entropia_original = entropia

total_conjunto = len(datos)

joven = datos[datos['edad'] <= 20]
adulto1 = datos[(datos['edad'] > 20) & (datos['edad'] <= 40)]
adulto2 = datos[(datos['edad'] > 40) & (datos['edad'] <= 50)]
mayor = datos[datos['edad'] > 50]

joven_poco = joven[joven['CantMateriasAprobadasPrimerCuatrimestre'] <= 2]
joven_medio = joven[(joven['CantMateriasAprobadasPrimerCuatrimestre'] > 2) & (joven['CantMateriasAprobadasPrimerCuatrimestre'] <= 4)]
joven_mucho = joven[joven['CantMateriasAprobadasPrimerCuatrimestre'] > 4]

adulto1_poco = adulto1[adulto1['CantMateriasAprobadasPrimerCuatrimestre'] <= 2]
adulto1_medio = adulto1[(adulto1['CantMateriasAprobadasPrimerCuatrimestre'] > 2) & (adulto1['CantMateriasAprobadasPrimerCuatrimestre'] <= 4)]
adulto1_mucho = adulto1[adulto1['CantMateriasAprobadasPrimerCuatrimestre'] > 4]

adulto2_poco = adulto2[adulto2['CantMateriasAprobadasPrimerCuatrimestre'] <= 2]
adulto2_medio = adulto2[(adulto2['CantMateriasAprobadasPrimerCuatrimestre'] > 2) & (adulto2['CantMateriasAprobadasPrimerCuatrimestre'] <= 4)]
adulto2_mucho = adulto2[adulto2['CantMateriasAprobadasPrimerCuatrimestre'] > 4]

mayor_poco = mayor[mayor['CantMateriasAprobadasPrimerCuatrimestre'] <= 2]
mayor_medio = mayor[(mayor['CantMateriasAprobadasPrimerCuatrimestre'] > 2) & (mayor['CantMateriasAprobadasPrimerCuatrimestre'] <= 4)]
mayor_mucho = mayor[mayor['CantMateriasAprobadasPrimerCuatrimestre'] > 4]

proporciones_joven_poco = fn.calcularProporcion(joven_poco, 'EstadoFinal', 'Continúa')
proporciones_joven_medio = fn.calcularProporcion(joven_medio, 'EstadoFinal', 'Continúa')
proporciones_joven_mucho = fn.calcularProporcion(joven_mucho, 'EstadoFinal', 'Continúa')

total_joven = len(joven)

proporciones_adulto1_poco = fn.calcularProporcion(adulto1_poco, 'EstadoFinal', 'Continúa')
proporciones_adulto1_medio = fn.calcularProporcion(adulto1_medio, 'EstadoFinal', 'Continúa')
proporciones_adulto1_mucho = fn.calcularProporcion(adulto1_mucho, 'EstadoFinal', 'Continúa')

total_audlto1 = len(adulto1)

proporciones_adulto2_poco = fn.calcularProporcion(adulto2_poco, 'EstadoFinal', 'Continúa')
proporciones_adulto2_medio = fn.calcularProporcion(adulto2_medio, 'EstadoFinal', 'Continúa')
proporciones_adulto2_mucho = fn.calcularProporcion(adulto2_mucho, 'EstadoFinal', 'Continúa')

total_adulto2 = len(adulto2)

proporciones_mayor_poco = fn.calcularProporcion(mayor_poco, 'EstadoFinal', 'Continúa')
proporciones_mayor_medio = fn.calcularProporcion(mayor_medio, 'EstadoFinal', 'Continúa')
proporciones_mayor_mucho = fn.calcularProporcion(mayor_mucho, 'EstadoFinal', 'Continúa')

total_mayor = len(mayor)

entropia_joven_poco = fn.calcularEntropia(proporciones_joven_poco, 'EstadoFinal', 'Continúa', joven_poco)
entropia_joven_medio = fn.calcularEntropia(proporciones_joven_medio, 'EstadoFinal', 'Continúa', joven_medio)
entropia_joven_mucho = fn.calcularEntropia(proporciones_joven_mucho, 'EstadoFinal', 'Continúa', joven_mucho)

entropia_adulto1_poco = fn.calcularEntropia(proporciones_adulto1_poco, 'EstadoFinal', 'Continúa', adulto1_poco)
entropia_adulto1_medio = fn.calcularEntropia(proporciones_adulto1_medio, 'EstadoFinal', 'Continúa', adulto1_medio)
entropia_adulto1_mucho = fn.calcularEntropia(proporciones_adulto1_mucho, 'EstadoFinal', 'Continúa', adulto1_mucho)

entropia_adulto2_poco = fn.calcularEntropia(proporciones_adulto2_poco, 'EstadoFinal', 'Continúa', adulto2_poco)
entropia_adulto2_medio = fn.calcularEntropia(proporciones_adulto2_medio, 'EstadoFinal', 'Continúa', adulto2_medio)
entropia_adulto2_mucho = fn.calcularEntropia(proporciones_adulto2_mucho, 'EstadoFinal', 'Continúa', adulto2_mucho)

entropia_mayor_poco = fn.calcularEntropia(proporciones_mayor_poco, 'EstadoFinal', 'Continúa', mayor_poco)
entropia_mayor_medio = fn.calcularEntropia(proporciones_mayor_medio, 'EstadoFinal', 'Continúa', mayor_medio)
entropia_mayor_mucho = fn.calcularEntropia(proporciones_mayor_mucho, 'EstadoFinal', 'Continúa', mayor_mucho)

entropia_ponderada_joven_poco = fn.calcularEntropiaPonderada(entropia_joven_poco, len(joven_poco), total_joven)
entropia_ponderada_joven_medio = fn.calcularEntropiaPonderada(entropia_joven_medio, len(joven_medio), total_joven)
entropia_ponderada_joven_mucho = fn.calcularEntropiaPonderada(entropia_joven_mucho, len(joven_mucho), total_joven)

entropia_ponderada_adulto1_poco = fn.calcularEntropiaPonderada(entropia_adulto1_poco, len(adulto1_poco), total_audlto1)
entropia_ponderada_adulto1_medio = fn.calcularEntropiaPonderada(entropia_adulto1_medio, len(adulto1_medio), total_audlto1)
entropia_ponderada_adulto1_mucho = fn.calcularEntropiaPonderada(entropia_adulto1_mucho, len(adulto1_mucho), total_audlto1)

entropia_ponderada_adulto2_poco = fn.calcularEntropiaPonderada(entropia_adulto2_poco, len(adulto2_poco), total_adulto2)
entropia_ponderada_adulto2_medio = fn.calcularEntropiaPonderada(entropia_adulto2_medio, len(adulto2_medio), total_adulto2)
entropia_ponderada_adulto2_mucho = fn.calcularEntropiaPonderada(entropia_adulto2_mucho, len(adulto2_mucho), total_adulto2)

entropia_ponderada_mayor_poco = fn.calcularEntropiaPonderada(entropia_mayor_poco, len(mayor_poco), total_mayor)
entropia_ponderada_mayor_medio = fn.calcularEntropiaPonderada(entropia_mayor_medio, len(mayor_medio), total_mayor)
entropia_ponderada_mayor_mucho = fn.calcularEntropiaPonderada(entropia_mayor_mucho, len(mayor_mucho), total_mayor)

ganancia_joven = entropia_original - (entropia_ponderada_joven_poco + entropia_ponderada_joven_medio + entropia_ponderada_joven_mucho)

ganancia_adulto1 = entropia_original - (entropia_ponderada_adulto1_poco + entropia_ponderada_adulto1_medio + entropia_ponderada_adulto1_mucho)

ganancia_adulto2 = entropia_original - (entropia_ponderada_adulto2_poco + entropia_ponderada_adulto2_medio + entropia_ponderada_adulto2_mucho)

ganancia_mayor = entropia_original - (entropia_ponderada_mayor_poco + entropia_ponderada_mayor_medio + entropia_ponderada_mayor_mucho)

print(ganancia_joven)

print(ganancia_adulto1)

print(ganancia_adulto2)

print(ganancia_mayor)