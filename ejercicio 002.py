import math
radio = float(input("digite radio del cilindro: "))
altura = float(input("digite altura del cilindro: "))

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def Area_cilindro(radio, altura):
    base_area = calcular_area_circulo(radio)
    lateral_area = 2 * math.pi * radio * altura
    return 2 * base_area + lateral_area

print("El área del cilindro es:", Area_cilindro(radio, altura))