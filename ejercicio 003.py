def calcular_media_edades(niños):
    return sum(niños) / len(niños)

num_niños = int(input("digite numero de niños: "))
niños = []

for i in range(num_niños):
    edad = int(input(f"digite edad del niño {i+1}: "))
    niños.append(edad)

media_edad = calcular_media_edades(niños)

print("media de edades es:", media_edad)