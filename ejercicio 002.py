import math
radio = float(input("digite radio del cilindro: "))
altura = float(input("digite altura del cilindro: "))

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_area_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    area_lateral = 2 * math.pi * radio * altura
    return 2 * area_base + area_lateral

print("El área del cilindro es:", calcular_area_cilindro(radio, altura))