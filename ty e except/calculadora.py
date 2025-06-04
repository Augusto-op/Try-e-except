def calculadora ():
    try:
        print("Calcualadora simples")
        num1 = input("Digite o primeiro numero: ")
        operador = input("Digite o operador (+, -, *, /): ")
        num2 = input("Digite o segundo numero: ")

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            resultado = num1 / num2
        else:
          print("Operdor invalido!")

        print("Resultado:", resultado)

    except ValueError:
        print("Erro: Entrada invalida! Por favor, digite numeros validos")
    except ZeroDivisionError:
        print("Erro: Divisao por zero nao e valida")
    except Exception as e:
        print("Ocorreu um erro inesperado", e)

    

calculadora()