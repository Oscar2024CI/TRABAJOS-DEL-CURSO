def calcular_cuadrados(numeros):
    return [n ** 2 for n in numeros]

num_elementos = int(input("digite número de elementos: "))
numeros = []

for i in range(num_elementos):
    num = int(input(f"digite el número {i+1}: "))
    numeros.append(num)

cuadrados = calcular_cuadrados(numeros)

print("La lista de cuadrados es:", cuadrados)