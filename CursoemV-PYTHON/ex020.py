from random import shuffle

# Exercício: Ordem Aleatória (Embaralhamento)
# Nota: Reutilizando variáveis de entrada para o exemplo
al1 = input('Digite o primeiro aluno: ')
al2 = input('Digite o segundo aluno: ')
al3 = input('Digite o terceiro aluno: ')
al4 = input('Digite o quarto aluno: ')

list2 = [al1, al2, al3, al4]
shuffle(list2)
print(f'A ordem de apresentação será: {list2}')
