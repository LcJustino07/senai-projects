# Construa um programa onde o usuario digitará dois numeros,
# utilizando passagem de parâmetros e, dentro da função,
# irá calcular a soma desses dois numeros.
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))

def somar(numero1, numero2):
    return numero1 + numero2

resultado = somar(numero1, numero2)
print(resultado)