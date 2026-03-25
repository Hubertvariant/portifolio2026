#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[[],[],[],],
          [[],[],[],],
          [[],[],[],]]

for pos_linha in range(len(matriz)):
    for pos_coluna in range(len(matriz[0])):
        while True:
            try:
                valor = int(input(f"Digite o valor da posição [{pos_linha},{pos_coluna}]: "))
                matriz[pos_linha][pos_coluna].append(valor)
                break
            except ValueError:
                print("Caractere invalido! Digite novamente")
                
for pos_linha in range(len(matriz)):
    for pos_coluna in range(len(matriz[0])):
        print(f"[ {matriz[pos_linha][pos_coluna]:^5} ]", end="")
    print("")