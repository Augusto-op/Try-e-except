def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Conversor de Temperatura")
    print("1 - Celsius para Kelvin")
    print("2 - Kelvin para Fahrenheit")

    try:
        opcao = int(input("Escolha a opção (1 ou 2): "))

        if opcao == 1:
            celsius = float(input("Digite a temperatura em Celsius: "))
            kelvin = celsius_para_kelvin(celsius)
            print(f"{celsius}°C = {kelvin:.2f}K")

        elif opcao == 2:
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            fahrenheit = kelvin_para_fahrenheit(kelvin)
            print(f"{kelvin}K = {fahrenheit:.2f}°F")

        else:
            print("Opção inválida! Escolha 1 ou 2.")

    except ValueError:
        print("Erro: Entrada inválida. Digite um número válido.")


main()