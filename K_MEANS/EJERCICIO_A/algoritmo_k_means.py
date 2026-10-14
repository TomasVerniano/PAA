import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('viviendas_habitadas_argentina.csv')

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['Viviendas Habitadas']])

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

lista_nombres = ['Pocas viviendas', 'Muchas viviendas', 'Cantidad normal de viviendas']

plt.figure(figsize=(10, 6))
for cluster in range(3):
    grupo = df[df['cluster'] == cluster]
    plt.scatter(grupo['Jurisdicción'], grupo['Viviendas Habitadas'], label=lista_nombres[cluster])
plt.xticks(rotation=45)
plt.xlabel('Jurisdicción')
plt.ylabel('Viviendas Habitadas')
plt.title('Segmentación de Jurisdicciones con K-Means')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()