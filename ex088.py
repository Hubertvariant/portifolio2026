#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

listaSorteios = []

while True:
    try:
        jogos = int(input("Quantos jogos vc quer sortear? "))
        break
    except ValueError:
        print("caractere invalido! Tente novamente")

for i in range(jogos):
    sorteio = []
    for i in range(6):
        while True:
            numero = randint(1, 60)
            if not numero in sorteio:
                sorteio.append(numero)
                break

    listaSorteios.append(sorted(sorteio))

for i in range(jogos):
    print(listaSorteios[i])
