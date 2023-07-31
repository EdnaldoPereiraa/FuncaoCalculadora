num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

def calculadora(num1, num2, op):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Não é possível dividir por zero.")
            return 0
    else:
        print("Operação inválida.")
        return 0

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)