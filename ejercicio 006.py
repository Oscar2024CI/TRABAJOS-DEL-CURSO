def decimal_a_binario(decimal):
    return bin(decimal).replace("0b", "")

def binario_a_decimal(binario):
    return int(binario, 2)

decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(decimal)
print("El número decimal", decimal, "en binario es:", binario)

binario = input("Ingrese un número binario: ")
decimal = binario_a_decimal(binario)
print("El número binario", binario, "en decimal es:", decimal)