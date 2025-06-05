try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura ** 2)

    print(f"Seu IMC é: {imc:.2f}")

except ValueError:
    print("Erro: Por favor, digite apenas números.")
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")
