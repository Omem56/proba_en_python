#debes modificar este programa para calcular todas las probabilidades de las figuras del poker en una mano
#ya casi todo funciona, solo falta modificar para la escalera
import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def proba_figuras_normales(manos, intentos, tamano_mano):
    VALORES_ORDENADOS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey','as']
    color = 0
    pares = 0
    tercia = 0
    poker = 0
    full_house = 0 
    escalera = 0
    escalera_de_color = 0
    flor_impperial = 0
    for mano in manos:
        valores = []
        palo = []
        rank_mano = [] #nos va a dar los valores que valen las cartas que salieron en la mano
        for carta in mano:
            valores.append(carta[1])
            palo.append(carta[0])
            rank_mano.append(VALORES_ORDENADOS.index(carta[1]))

        
        segundo_counter=dict(collections.Counter(palo))
        counter = dict(collections.Counter(valores))
        full_par = False
        full_tercia = False
        bandera_color = False
        bandera_escalera = False
        color_straight = False
        for val in counter.values():
            if val == 2:
                pares += 1
                full_par = True
            if val == 3:
                tercia += 1
                full_tercia = True
            if val == 4:
                poker += 1
        if full_par and full_tercia:
                full_house += 1
        
        for val in segundo_counter.values():
            if val == 5:
                color += 1
                bandera_color = True
        #vamos a checar la escalera
        zipped = zip(mano, rank_mano)
        mano_ordenada = list(sorted(zipped, key = lambda x:x[1]))
        if mano_ordenada[-1][1] - mano_ordenada[0][1] == tamano_mano - 1:
            escalera += 1
            bandera_escalera = True

        if bandera_color and bandera_escalera:
            escalera_de_color += 1
            color_straight = True

        
        stop = 12 - tamano_mano #valor que nos permite determinar escalera desde arriba dependiendo del tamano de la mano
        if color_straight and valores==VALORES_ORDENADOS[-1:stop:-1]:
            flor_impperial += 1




    return (pares / intentos, tercia/intentos, poker/intentos, full_house/intentos, color/intentos, escalera/intentos, escalera_de_color/intentos, flor_impperial/intentos)


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    par, triada, cuadruple, full, color, escaleras, escaleras_color, escalera_real = proba_figuras_normales(manos, intentos, tamano_mano)
    print(f'la probabilidad de sacar un par es {par}')
    print(f'la probabilidad de sacar una tercia es {triada}')
    print(f'la probabilidad de sacar un poker es {cuadruple}')
    print(f'la probabilidad de sacar un full house es {full}')
    print(f'la probabilidad de sacar un color es {color}')
    print(f'la probabilidad de sacar un escalera es {escaleras}')
    print(f'la probabilidad de sacar un escalera de color es {escaleras_color}')
    print(f'la probabilidad de sacar una flor imperial es {escalera_real}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)