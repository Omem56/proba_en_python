# Este es un codigo que simula el lanzamiento de dos dados y su suma, al cambiar las realizaciones se puede ver como cambia la distribucion de las sumas
import random
from bokeh.charts import Histogram, output_file, show

class Dado:
    def __init__(self, numero_de_dados, numero_de_lados):
        self.numero_de_dados = numero_de_dados
        self.numero_de_lados = numero_de_lados
    
    def tirar_dados(self):
        resultado = []
        for _ in range(1, self.numero_de_dados + 1):
            resultado.append(random.randint(1, self.numero_de_lados))
        return resultado

if __name__ == "__main__":
    dado_6 = Dado(2, 6)
    #realizacion = dado_6.tirar_dados()
    #print(realizacion)
    #print(sum(realizacion))
    sumas = []
    tiradas = 10000
    for _ in range(tiradas):
        realizacion = dado_6.tirar_dados()
        suma = sum(realizacion)
        sumas.append(suma)
    print(len(sumas))

    grafica = Histogram(sumas, title='Suma de dos dados con 10000 realizaciones')

    output_file('suma_de_dados.html')
    show(grafica)
