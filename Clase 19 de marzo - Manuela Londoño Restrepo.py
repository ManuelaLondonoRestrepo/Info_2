#Primero se importan las librerías a emplear

import pandas as pd
import numpy as np

#La series son matrices capaz de contener cualquier tipo de datos
# #Cuando trabajemos en pandas vamos a tener una estructura como esta:
#En una serie tendremos columnas y filas, las columnas normalmente 
# contienen el mismo tipo de dato

#serie tiene una columna
  #X1(Indices de las columnas)
#1 
#2
#3 (Indices de las filas)

#dataframe tiene más de una columna
  #X1(Indices de las columnas)  X2
#1                            #1
#2                            #2
#3 (Indices de las filas)     #3

#Los índices no tienen que ser numéricos ni estar organizados pero siempre debe haber índice

#Los datos pueden ser muchas cosas diferentes, diccionario de python, 
#un ndarray o un valor escalar

#Si el dato es un array, el índice debe tener la misma longitud que los 
# datos. Si no se pasa ningún índice, se creará automáticamente uno con valores [0,...,len(data - 1)]

#Para crear una serie, se realiza lo siguiente s = pd.Series(el array de datos, los índices)
#Por ejemplo s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd'])

s = pd.Series(np.random.randn(5), index=[1,2,3,4,5])

#Para visualizar los índices de la serie utilizamos s.index, este muestra los índices y el tipo de dato que son

#También puedo crear una serie a partir de un diccionario. Primero debo crear el diccionario y pasarlo luego a la serie
#d ={'a': 1, 'b': 2, 'c': 4}
#Creo una serie s = pd.series(d, index=[a, c,b])
#El orden de la serie será el que indiquen los índices y no el de las claves de los diccionarios

d ={'a': 1, 'b': 2, 'c': 4}
s = pd.Series(d, index=['a', 'c','b'])

#También se puede dejar sin índice y tomará el orden de las claves del diccionario

s= pd.Series(d)

#Cuando el dato es un escalar se le pasa el escalar y ciertos índices. La serie asignará el mismo valor escalar a todos
#los índices

s = pd.Series(3, index=[1, 3, 6])

#Acceder a distintas pocisiones de la serie es posible de la siguiente forma
s[0]
s[-1]

#Operaciones o cambio de orden de la serie
#completar
s.median()

#Para visualizar los datos de la serie en forma de array podemos usar series.to_numpy()
s.to_numpy()

#OPeraciones. Es posible realizar s+s(suma), s*2(multiplicación), s/28(División), np.exp(s) aplicar métodos de numpy
s[1:]+ s[:-1]
#Desde el uno hasta el final, todos menos el último

#El método a.dropnan() quita los valore vacíos del resultado de la operación a que se le pase

#LA PRINCIPAL HERRAMIENTA DE PANDAS ES SUBIR ARCHIVOS DE TEXTO Y MODIFICARLOS. por eso, esta librería tiene una función para convertir datros de texto en objetos como los anteirore
#Hay una forma para subir cada tipo de archivo (json, txt, csv, ets
# 
# Ejemplo mini-mental 

#Cargar un archivos

import os
import glob

current = os.getcwd #Indico dónde estoy parada
#Determino 
#Ahora creo una lista con solo los archivos del tipo que me interesa (en este caso csvg)
file = glob.glob(current+'/*.csv') #Así accedo a los archivos csv de la ruta en la que estoy parada
#Agora voy a leer el archivo que me interesa.- Lo asigno a una variable y pongo
alzheimer = pd.read_csv(file[0] , sep =';')
#(ruta del archivo o posición en la lista de archivos file, caracter en el que se va a separar)
#Ya queda el archivo subido como un objeto de pandas (dataframe porque tiene más de una columna)

#Luego, puedo obtener el tamaño del dataframe 
alzheimer.size

#Para acceder a los índices de las columnas
alzheimer.columns
#Para acceder a una sola columna con sus valores
#alzheimer['indice de la columna']
alzheimer['age']

#Describe saca las medidas estadísticas de los datos de cada columna 
alzheimer.describe()
alzheimer.describe().T #Saca la transpuesta

#Para acceder a la info de una fila se usa
alzheimer.loc[1] #Dentro de los corchetes el índice de la fila

#Arrojará todos los valor de la fila con el nombre de la columna al que pertenecen

#Podemos crear un archivo de copia para editar sin dañar nada
#Simplemente copio el archivo asignándolo a una variable diferente
alzheimer_copy = alzheimer.copy()

alzheimer_copy = alzheimer_copy.reset_index()

#Para eliminar una columna le digo 
alzheimer_copy= alzheimer_copy.drop(['index'], axis = 1)
#Tmbién puedo borrar con del 
del alzheimer_copy['index']

#Para borrar una fila 
alzheimer_copy= alzheimer_copy.drop(['index'], axis = 0)

#Voy a crear un dataframe que va a alamacenar a solo los sujetos que sean de edad mayior a setenta
alzheimer_edad_70 = alzheimer[(alzheimer['Age'] >= 70)]
print(alzheimer_edad_70)
print(alzheimer_edad_70.shape)
alzheimer_educación = alzheimer[(alzheimer['Educ'] < 14)]

#.mean() y graficar con sns.barplot() y los otros plot