#Forma explícita

import matplotlib.pyplot as plt
import numpy as np

#Defino cada eje
x = np.linspace(0,2*np.pi, 200)
y = np.sin(x)

#Creo el gráfico
fig, ax = plt.subplots()
ax.plot(x, y, label = "sen(x)")
plt.show()

#Pongo nombre la los ejes y a la gráfica
ax.set_xlabel('eje x')
ax.set_ylabel('eje y')
ax.set_title('Grafica de la función seno(x)')

#Agrego la leyenda
ax.legend()
plt.show()

ax.annotate('local max', xy=(2.1), xytext=(3,1,5), arrowprops=dict(facecolor='black', shrink=0.05))