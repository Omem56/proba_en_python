#calcular pi mediante estimaciones probabilisticas

import random
import math
from estadisticos import desviacion_estandar, media

def aventar_agujas(numero_agujas):
    dentro_circulo = 0
    for _ in range(numero_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            dentro_circulo += 1
        
    return (4 * dentro_circulo) / numero_agujas

def estimacion(numero_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados  = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'El estimado = {round(media_estimados, 5)}, sigma = {round(sigma, 5)}')
    print(f'agujas = {numero_agujas}')

    return (media_estimados, sigma)

def estimar_pi(precision, numero_de_intentos):
    numero_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_agujas, numero_de_intentos)
        numero_agujas *= 2

    return media

if __name__ == "__main__":
    estimar_pi(0.01, 1000)