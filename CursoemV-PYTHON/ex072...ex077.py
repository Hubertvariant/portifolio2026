from random import randint

contCor = randint(0,1)
cor = ('\033[1;36m', '\033[1;33m')

ex = ' '
while not ex.isnumeric():
    ex = str(input('Digite o número do EXERCICIO: '))
ex = int(ex)
if ex == 72:
    print(f'{cor[contCor]}{'072':=^40}\033[m')
    extenco = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
    numero = ' '
    while True:
        numero = str(input('Digite um número de 0 a 20: '))
        numero = int(numero)
        if numero < 0 or numero > 20:
            print('Tente novamete! ', end='')
        else:
            break

    print(f'O número {numero} em extenço: {extenco[numero]}')
elif ex == 73:
    print(f'{cor[contCor]}{'073':=^40}\033[m')
    print('Campeonato Brasileiro de Futebol')
    times = ('Flamengo', 'Palmeiras', 'Cruseiro', 'Mirassol', 'Fluminense', 'Botafogo','Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlétioco-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')
    while True:
        print('''A)Mostrar a lista.
B)Apenas os 5 Primeiros colocados.
C)Os útimos 4 colocados da tabela.
D)Uma lista com os times em ordem alfabetica.
E)Procure em que posição está o seu time.
F)Sair do Menu.
''')
        opcao = str(input('Digite sua escolha: ')).strip().upper()[0]
        if opcao == 'F':
            break
        else:
            if opcao == 'A':
                print('Todos os Times em ordem.')
                for c in range(0, len(times)):
                    print('='*20)
                    print(f'{c + 1} {times[c]}')
                print(' ')
            elif opcao == 'B':
                for c in range(0,5):
                    print('='*20)
                    print(f'{c+1}° {times[c]}')
            elif opcao == 'C':
                for c in range(16, 20):
                    print('='*20)
                    print(times[c])
                print(' ')
            elif opcao == 'D':
                timesOrdenados = sorted(times)
                for c in timesOrdenados:
                    print('='*20)
                    print(c)
                print(' ')
            elif opcao == 'E':
                print(f'{times.index('Bahia') + 1}° Bahia')
            else:
                print('Opção inválida. Tente novamente.')

elif ex == 74:
    print(f'{cor[contCor]}{'074':=^40}\033[m')
    numero = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
    print('Os valores sorteados foram', end=' ')
    for num in numero:
        print(num, end=' ')
    print(f'\nO maior valor foi {max(numero)}')
    print(f'O menor valor foi {min(numero)}')

elif ex == 75:
    print(f'{cor[contCor]}{'075':=^40}\033[m')
    for cont in range(0, 4):
        num = ''
        while not num.isnumeric():
            num = input('Digite um valor:')
        num = int(num)
        if cont == 0:
            n1 = num
        elif cont == 1:
            n2 = num
        elif cont == 2:
            n3 = num
        elif cont == 3:
            n4 = num
    valores = (n1, n2, n3, n4)
    print(f'O número 9 apareceu {valores.count(9)}')
    if 3 in valores:
        print(f'O número 3 apareceu na {valores.index(3) + 1}° posição.')
    else:
        print('O número 3 nao foi digitado.')
    cont = 0
    for n in valores:
        if n % 2 == 0:
            cont += 1
    print(f'Os valores pares digitados foram {cont}')

elif ex == 76:
    print(f'{cor[contCor]}{'076':=^40}\033[m')
    lista_de_materiais = ('lapis', 1.00, 'cola', 3.00, 'tesoura', 3.00, 'bolsa', 65.00, 'caderno', 24.00, 'caneta', 1.50)
    print('-=-' * 20)
    print(f'{'LISTA DE MATERIAIS':^40}')
    print('-=-' * 20)
    for prod in range(0, len(lista_de_materiais), 2):
        print(f'{lista_de_materiais[prod]:.<30}R${lista_de_materiais[prod + 1]:>6.2f}', end='\n')
    print('-=-' * 20)

elif ex == 77:
    print(f'{cor[contCor]}{'077':=^40}\033[m')
    palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
    vogais = ('a', 'e', 'i', 'o', 'u')
    for p in palavras:
        print(f'Na palavra {cor[randint(0, 1)]}{p.upper()}\033[m temos ', end='')
        for l in p.lower(): 
            if l in vogais:
                print(l, end=' ')
        print()