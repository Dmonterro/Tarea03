numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

def suma_es_par(num1, num2):
    suma = num1 + num2
    return suma % 2 == 0


resultado = suma_es_par(numero1, numero2)

print(f"¿La suma de {numero1} y {numero2} es par o impar? {resultado}")