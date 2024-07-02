num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

def maximo_comun_divisor(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def minimo_comun_multiplo(a, b):
    return a * b // maximo_comun_divisor(a, b)

mcd = maximo_comun_divisor(num1, num2)
mcm = minimo_comun_multiplo(num1, num2)

print("El máximo común divisor de", num1, "y", num2, "es:", mcd)
print("El mínimo común múltiplo de", num1, "y", num2, "es:", mcm)