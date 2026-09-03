numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))

operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    resultado = numero1 + numero2
    print("Resultado: ", resultado)
elif operador == "-":
    resultado = numero1 - numero2
    print("Resultado: ", resultado)
elif operador == "*":
    resultado = numero1 * numero2
    print("Resultado: ", resultado)
elif operador == "/":
    resultado = numero1 / numero2
    print("Resultado: ", resultado)
else:
    print("Operador inválido!")