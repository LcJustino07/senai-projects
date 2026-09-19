# calcular a sequencia de fibonacci ate 2000
# não tem entrada de usuario

antepenultimo = 0
penultimo = 1

print(f'{antepenultimo}')
print(f'{penultimo}')
for i in range(0,2000):
    i = antepenultimo + penultimo
    if i < 2000:
        print(f'{i}')
antepenultimo = penultimo
penultimo = i

anterior = 0
atual = 1 
proximo = anterior + atual # 1
print(anterior)
print(atual)
print(proximo)
while(proximo <= 2000):
    anterior = atual
    atual - proximo
    proximo = anterior + atual
    print(proximo)