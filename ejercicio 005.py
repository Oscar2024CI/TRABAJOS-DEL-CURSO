import math

def calcular_estadisticas(numeros):
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    desviacion_tipica = math.sqrt(varianza)
    return {"varianza": varianza, "desviacion_tipica": desviacion_tipica}

num_elementos = int(input("Ingrese el número de elementos: "))
numeros = []

for i in range(num_elementos):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

estadisticas = calcular_estadisticas(numeros)

print("Varianza:", estadisticas["varianza"])
print("Desviación típica:", estadisticas["desviacion_tipica"])