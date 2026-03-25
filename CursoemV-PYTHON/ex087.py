#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:

matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
totSoma = coluna_3_soma = maior = 0
for pos_linha in range(len(matriz)):
    for pos_coluna in range(len(matriz[pos_linha])):
        valor = int(input(f'Digite um valor para [{pos_linha}, {pos_coluna}]: '))
        matriz[pos_linha][pos_coluna] = valor
        if valor % 2 == 0:
            totSoma += valor

        if pos_coluna == 2:
            coluna_3_soma += valor
        
        if pos_linha == 1:
            if valor > maior:
                maior = valor

for pos_linha in range(len(matriz)):
    for pos_coluna in range(len(matriz[pos_linha])):
        print(f'[{matriz[pos_linha][pos_coluna]:^5}]', end=' ')
    print()

#A) A soma de todos os valores pares digitados.
print(f"A soma de todos os valores pares digitados: {totSoma}")

# B) A soma dos valores da terceira coluna.
print(f"A soma dos valores da terceira coluna: {coluna_3_soma}")

# C) O maior valor da segunda linha.
print(f"O maior valor da segunda linha: {maior}")
