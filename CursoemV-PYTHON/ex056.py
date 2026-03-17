from time import sleep

print(f'''\033[33;1m{"=" * 10}
{"ex056":^10}
{"=" * 10}\033[m''')
sleep(1)

soma = 0
homemVelho = 0
nomeVelho = ''
mulheresNovas = 0

print('\033[1mFORMULARIO!')
for c in range(0, 4):
    print('-=' * 10)
    nome = str(input('Digite o seu nome: ')).capitalize().strip()
    idade = int(input('Digite sua idade: '))
    sexo = int(input('''Digite:
[1]Masculino
[2]Feminino
Digite o número do seu sexo: '''))
    
    soma += idade
    if sexo == 1:
        if idade > homemVelho:
            homemVelho = idade
            nomeVelho = nome
    else:
        if idade < 21:
            mulheresNovas += 1

print(f'''A média da idade do grupo: {soma / 4}
O homem mais velho é o {nomeVelho} com {homemVelho} anos
Número de mulheres abaixo de 21 anos: {mulheresNovas}''')