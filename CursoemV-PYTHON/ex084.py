#Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:

cadastrosDePessoas = []
maiorPesos = []
menorPesos = []
somaDosPesos = 0
while True:

    nome = input("Digite seu nome: ").strip().capitalize()
    peso = float(input("Digite seu peso: "))

    pessoa = [nome, peso]
    somaDosPesos += peso

    cadastrosDePessoas.append(pessoa)
    
    opcao = ""
    while opcao != "n" and opcao != "s":
        opcao = str(input("Deseja continuar:[S/N] ")).strip().lower()
    if opcao.startswith("n"):
        break

pesoMedio = somaDosPesos / len(cadastrosDePessoas)

for pessoas in cadastrosDePessoas:
    if pessoas[1] > pesoMedio:
        maiorPesos.append(pessoas)
    elif pessoas[1] < pesoMedio:
        menorPesos.append(pessoas)

# A) Quantas pessoas foram cadastradas.
print(f"O número de pessoas cadastradas foi {len(cadastrosDePessoas)}")

# B) Uma listagem com as pessoas mais pesadas.
print(f"A lista de pessoas mais pesadas cadastradas:")
for pessoas in maiorPesos:
    print(f"{pessoas[0]} com {pessoas[1]}kg")

# C) Uma listagem com as pessoas mais leves.
print(f"A lista de pessoas mais leves cadastradas:")
for pessoas in menorPesos:
    print(f"{pessoas[0]} com {pessoas[1]}kg")
