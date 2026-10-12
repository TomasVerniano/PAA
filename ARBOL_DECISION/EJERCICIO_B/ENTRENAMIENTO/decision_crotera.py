import math
import pandas as pd

excel_entrenamiento = pd.read_csv("ENTRENAMIENTO/TablaPrediccionAbandono-Entrenamiento.csv")

#datos del conjunto de entrenamiento
total_personas = len(excel_entrenamiento['edad'])

continua_total= len(excel_entrenamiento[excel_entrenamiento['EstadoFinal'] == 'Continúa'])
abandona_total= len(excel_entrenamiento[excel_entrenamiento['EstadoFinal'] == 'Abandonó'])


#entropia
p_cont = continua_total / total_personas
p_aban = abandona_total / total_personas

hs = -(p_cont * math.log2(p_cont) + p_aban * math.log2(p_aban))


"""
-------------------------------------------------------------------------------
grupos:
-edad: Joven (≤30), Adulto (31–50), Mayor (>50)
-genero: f, m
-carreras: pymes, contable, radiologia, industrial, enfermeria, IA, higiene, sistemas, multimedial   : (Total 9)
-Promedio primer cuatri: aprobado (≥7), desaprobado(≤6)
-Cant materias aprobadas:  aprobado (≥7), desaprobado(≤6)
-Cant materias desaprobadas: aprobado (≥7), desaprobado(≤6)
-asistencia promedio: asiste (≥90%), regular (≥70% and <90%), ausente ()
"""
carreras = pd.unique(excel_entrenamiento['carrera'])
#print(carreras)