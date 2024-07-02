a = float(input("digite primer numero: "))
b = float(input("digite segundo numero: "))
operacion = input("digite la operacion (+, -, *, /): ")


def operaciones_basicas():
    
    if operacion == "+":
        resultado = a + b
    elif operacion == "-":
        resultado = a - b
    elif operacion == "*":
        resultado = a * b
    elif operacion == "/":
        if b!= 0:
            resultado = a / b
        else:
            print("no puede dividir entre cero")
            return
    else:
        print("operación no válida")
        return

    print(f"El resultado de la operacion {operacion} es: {resultado}")

operaciones_basicas()