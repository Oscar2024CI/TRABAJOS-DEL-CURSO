def frecuencia_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def palabra_mas_repetida(frecuencia):
    palabra_mas_repetida = max(frecuencia, key=frecuencia.get)
    return (palabra_mas_repetida, frecuencia[palabra_mas_repetida])

cadena = input("Ingrese una cadena de caracteres: ")
frecuencia = frecuencia_palabras(cadena)
print("Frecuencia de palabras:", frecuencia)

palabra_mas_repetida, frecuencia = palabra_mas_repetida(frecuencia)
print("La palabra más repetida es:", palabra_mas_repetida, "Con una frecuencia de:", frecuencia)