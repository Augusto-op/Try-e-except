reais = input('DIgite a quantia que você quer converter:')
dolar = 5.59

try:
    reais = float(reais)
    print(f'A convertido em reais é: {dolar * reais}')
except:
    print('Tente novamente com números, por favor!')