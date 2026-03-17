from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"073":=^40}\033[m')
print('Campeonato Brasileiro de Futebol')

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 
         'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitória', 
         'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')

while True:
    print('''\n[A] Mostrar a lista completa
[B] Apenas os 5 primeiros colocados
[C] Os últimos 4 colocados da tabela
[D] Lista em ordem alfabética
[E] Posição do time "Bahia"
[F] Sair do Menu''')
    
    opcao = str(input('Digite sua escolha: ')).strip().upper()[0]
    
    if opcao == 'F':
        break
    elif opcao == 'A':
        print('\nTodos os Times:')
        for pos, time in enumerate(times):
            print(f'{pos + 1}º {time}')
    elif opcao == 'B':
        print('\nOs 5 primeiros:')
        for t in times[:5]:
            print(t)
    elif opcao == 'C':
        print('\nOs 4 últimos:')
        for t in times[-4:]:
            print(t)
    elif opcao == 'D':
        print('\nOrdem Alfabética:')
        for t in sorted(times):
            print(t)
    elif opcao == 'E':
        posicao = times.index('Bahia') + 1
        print(f'\nO Bahia está na {posicao}ª posição.')
    else:
        print('Opção inválida. Tente novamente.')