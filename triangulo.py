# Passo 1-> ter 3 valores numericos reais que representam lados do triangulo
lado1 = float(input('Digite um lado1: '))
lado2 = float(input('Digite um lado2: '))
lado3 = float(input('Digite um lado3: '))

# Verificar a condição de existência geométrica:
condicao = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

#Classificar o triangulo em equilatero, isosceles ou escaleno
if condicao:
    if lado1 == lado2 == lado3:
        print('Equilatero')

    elif lado1 != lado2 != lado3:
        print('Escaleno')

    elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print('Isosceles')

else:
    print('Não é um triangulo')