#Primero importo la librería numpy como np
import numpy as np

#Para llamar a los métodos de numpy debo poner np.nombre del método()
#Miremos el método arange 
a = np.arange(15) #Número de elementos
print(a) #me genera una serie de núeros desde cero hasta el número antes del que especifiqué como parámetro al usar el método

#Para volverlo matriz, utilizo np.reshape(número de filas, número de columnas)
#El número de filas multiplicado por el número de columnas debe dar siempre el número de elementos
b = np.arange(20).reshape(5,4)
print(b)

#Para crear una matriz puedo usar np.array y pasarle las filas de la matriz con sus componentes entre corchetes 
#y estos separados por comas
c = np.array([[1,2], [3,4]])
print(c)

#También puedo pasarle el tipo de dato que quiero que sean, así
d = np.array([[12,14,16], [17,19,21]], dtype=str) #tambnién puedo poner complex para que los vuelva complejos, 
#float para que los ponga decimales y así
print(d)

print(a.shape)
print(b.shape) #Para saber el número de filas y columnas de un array

print(a.size)
print(b.size) #Para saber la cantidad de elementos que el array tiene en su interior

#Todos los elementos de un array deben ser del mismo tipo de dato
print(a.dtype)
print(b.dtype) #Para saber el tipo de dato de los elemento que tengo dentro de un array