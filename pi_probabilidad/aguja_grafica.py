#visualizacion de la funcion aventar_agujas
from bokeh.io import output_file
from bokeh.plotting import figure, show
import random
import math


def aventar_agujas(numero_agujas):
    puntos_adentro_x = []
    puntos_adentro_y = []
    puntos_afuera_x = []
    puntos_afuera_y = []
    for _ in range(numero_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            puntos_adentro_x.append(x)
            puntos_adentro_y.append(y)

        else:
            puntos_afuera_x.append(x)
            puntos_afuera_y.append(y)

    output_file('agujas_en_circulo.html', title='random pi')
    fig = figure()
    fig.circle(x = puntos_adentro_x, y =  puntos_adentro_y, color = '#4292c6', size = 5)
    fig.circle(x = puntos_afuera_x, y =  puntos_afuera_y, color = '#f03b20', size = 5)
    show(fig)

if __name__ == "__main__":
    aventar_agujas(10000)
