from random import randint
contCor = randint(0,1)
cor = ('\033[1;36m', '\033[1;33m')
ex = ''
while True:
    ex = str(input('Digite o número do EXERCICIO: '))
    if ex.isnumeric() and 78 <= int(ex) <= 89:
        ex = int(ex)
        break
    else:
        print('ERRO! Tente novamente.', end=' ')

if ex == 78:
    print(f'{cor[contCor]}{'78':=^40}\033[m')
    valores = []
    for c in range(0, 5):
        while True:
            valores.append(str(input(f'Digite o {c + 1}° valor: ')))
            if valores[c].isnumeric():
                int(valores[c])
                break
            else:
                print('ERRO! Tente novamente!', end=' ')
                valores.pop()
    print(f'Os valores digitados foram{valores}.')
    print(f'O maior valor {max(valores)} está nas posições', end=' ')
    for c, v in enumerate(valores):
        if v == max(valores):
            print(c, end='... ')
    print(f'\nO menor valor {min(valores)} está nas posições', end=' ')
    for c, v in enumerate(valores):
        if v == min(valores):
            print(c, end='... ')

elif ex == 79:
    print(f'{cor[contCor]}{'79':=^40}\033[m')
    num = []
    cont = 0
    verbo = 'um'
    while True:
        while True:
            add = str(input(f'Digite {verbo} numero: '))
            
            if add.isnumeric():
                int(add)
                if add in num:
                    print('Valor duplicado! Não vou adicionar.', end=' ')
                    verbo = 'outro'
                else:
                    print('Adicionado com sucesso...')
                    num.append(add)
                    break
            else:
                print('ERRO! Caractere invalido. ', end='')
        cont += 1
        chevron = ''
        while True:
            chevron = str(input('Deseja continuar?[S/N] '))
            if chevron in 'NnSs':
                break
        if chevron in 'Nn':
            print('Obrigado por utilizar o nosso programa!')
            break
        elif chevron in 'Ss':
            verbo = 'outro'
    print('A lista com números únicos ', sorted(num))
        
elif ex == 80:
    print(f'{cor[contCor]}{'80':=^40}\033[m')
    listaDeValores = []
    for c in range(0, 5):
        add = int(input('Digite o valor: '))
        if c == 0 or add > listaDeValores[-1]:
            listaDeValores.append(add)
            print('Adicionado no final da lista.')
        else:
            for pos, v in enumerate(listaDeValores):
                if add <= v:
                    listaDeValores.insert(pos, add)
                    print(f'Adicionado na {pos} da lista')
                    break
    print(listaDeValores)

elif ex == 81:
    print(f'{cor[contCor]}{'81':=^40}\033[m')
    ListaDeNum = []
    verbo = 'um'
    c = 0
    while True:
        add = str(input(f'Digite {verbo} número: '))
        if add.isnumeric():
            int(add)
            if c == 0 or add > ListaDeNum[0]:
                ListaDeNum.insert(0, add)
            elif add < ListaDeNum[-1]:
                ListaDeNum.append(add)
            else:
                for pos, v in enumerate(ListaDeNum):
                    if add >= v:
                        ListaDeNum.insert(pos, add)
                        break
            c = 1
            chevron = ''
            while True:
                chevron = str(input('Deseja continuar?[S/N] ')).lower().strip()
                if chevron in 'nNSs':
                    break
            if chevron in 'Nn':
                break
            else:
                verbo = 'outro'
        else: 
            print('Digito invalido.Tente novamente.', end=' ')
    print(f'Você digitou {len(ListaDeNum)} elementos.')
    print(f'Os valores em ordem decrescente são {ListaDeNum}.')
    print('O valor 5 ', end='')
    if 5 not in ListaDeNum:
        print('não faz parte da lista!')
    else:
        print('faz parte da lista!')

elif ex == 82:
    print(f'{cor[contCor]}{'82':=^40}\033[m')
    impares = []
    pares= []
    while True:
        add = ''
        while not add.isnumeric():
            add = str(input('Digite um valor: '))
        add = int(add)
        if add % 2 == 0:
            pares.append(add)
        else:
            impares.append(add)
        while True:
            continua = str(input('Deseja continuar?'))
            if continua in 'SsNn':
                break
        if continua in 'nN':
            break

    listaCompleta = impares + pares
    print('A lista completa: ', listaCompleta)
    print('Números pares: ', pares)
    print('Números ìmpares: ', impares)

elif ex == 83:
    print(f'{cor[contCor]}{'83':=^40}\033[m')
    print('Validando expreções numericas')
    expreção = str(input('Digite uma expreção: ')).strip()
    pilha = []
    for simb in expreção:
        if simb == '(':
            pilha.append(simb)
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(simb)
                break
    if len(pilha) == 0:
        print(f'A expreção {expreção} é valida!')
    else:
        print(f'A expreção {expreção} não é valida!')
