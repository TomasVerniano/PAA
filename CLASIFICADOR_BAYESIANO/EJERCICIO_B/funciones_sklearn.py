from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

def separarCaracteristicasEtiquetas(datos):

    conjuntos = datos.values.tolist()

    x = []
    y = []

    for item in conjuntos:
        x.append(item[0])
        y.append(item[1])

    return (x, y)

def entrenarModelo(x, y):

    #Convertir texto en vectores de frecuencia
    vectorizador = CountVectorizer()
    x_vectorizado = vectorizador.fit_transform(x)

    #Dividir en entrenamiento y prueba
    x_train, x_test, y_train, y_test = train_test_split(x_vectorizado, y, test_size=0.3, random_state=42)

    #Entrenar el clasificador Naive Bayes
    modelo = MultinomialNB()
    modelo.fit(x_train, y_train)

    return (modelo, x_train, x_test, y_train, y_test, vectorizador)

def evaluarModelo(modelo, x_test, y_test):

    y_pred = modelo.predict(x_test)

    return(y_pred, classification_report(y_test,y_pred), confusion_matrix(y_test, y_pred))

def predecir(datos, modelo, vectorizador):

    datos_vectorizados = vectorizador.transform(datos)

    predicciones = modelo.predict(datos_vectorizados)

    for noticia, prediccion in zip(datos, predicciones):
        print(f'Noticia: "{noticia}" -> Clasificacion: {prediccion}')
