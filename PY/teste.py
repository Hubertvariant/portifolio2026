import matplotlib.pyplot as plt

listaAlunos = []
while True:
    opcao = ' '
    if opcao == 0:
        break
    while True:
        aluno = []
        while True:
            nome = ''
            while not nome.isalpha():
                nome = str(input('Digite seu nome: ')).strip().lower()
            idade = ''
            while not idade.isnumeric():
                idade = str(input('Digite sua idade: ')).strip()
            idade = int(idade)
            sexo = ''
            while sexo != 'M' and sexo != 'F':
                sexo = str(input('Digite seu sexo:[M/F] ')).strip().upper()[0]
            indice = ''
            while not indice.isnumeric():
                indice = str(input('Digite o indice do aluno: ')).strip()
            indice = int(indice)
            corrigir = ''
            while corrigir != 'S' and corrigir != 'N':
                corrigir = str(input('\033[1;31mDeseja corrigir os dados?[S/N] \033[m')).strip().upper()
            if corrigir in 'N':
                break
        aluno.append(nome)
        aluno.append(idade)
        aluno.append(sexo)
        aluno.append(indice)
        if not listaAlunos or indice > listaAlunos[-1][3]:
            listaAlunos.append(aluno[:])
        else:
            for pos, v in enumerate(listaAlunos):
                if indice <= v[3]:
                    listaAlunos.insert(pos, aluno[:])
                    break
        continuar = ''
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('\033[1;31mDeseja continuar?[S/N] \033[m')).strip().upper()[0]
        if continuar in 'N':
            break
    while True:
        print('Menu de opções')
        print('1 - Ver alunos cadastrados')
        print('2 - Ver alunos de idade X')
        print('3 - Ver alunos de sexo X')
        print('4 - Ver alunos que começa com a letra X')
        print('5 - Ver alunos por idade em um grafico')
        print('6 - Adicionar alunos')
        print('0 - Sair')
        print('=' * 30)
        opcao = ' '
        while not opcao.isnumeric():
            opcao = str(input('Digite uma opção: ')).strip()[0]        
        opcao = int(opcao)
        if opcao == 1:
            for cont in range(0, len(listaAlunos)):
                print('=' * 30)
                print(f'''indice: {listaAlunos[cont][3]}/ nome: {listaAlunos[cont][0]}/ idade: {listaAlunos[cont][1]}/ sexo: {listaAlunos[cont][2]}''')
                print('=' * 30)
        elif opcao == 2:
            idade = int(input('Digite a idade: '))
            for cont in range(0, len(listaAlunos)):
                if idade == listaAlunos[cont][1]:
                    print('=' * 30)
                    print(f'''indice: {listaAlunos[cont][3]}/ nome: {listaAlunos[cont][0]}/ idade: {listaAlunos[cont][1]}/ sexo: {listaAlunos[cont][2]}''')
                    print('=' * 30)
        elif opcao == 3:
            sexo = str(input('Digite o sexo:[M/F] ')).strip().upper()[0]
            for cont in range(0, len(listaAlunos)):
                if sexo == listaAlunos[cont][2]:
                    print('=' * 30)
                    print(f'''indice: {listaAlunos[cont][3]}/ nome: {listaAlunos[cont][0]}/ idade: {listaAlunos[cont][1]}/ sexo: {listaAlunos[cont][2]}''')
                    print('=' * 30)
        elif opcao == 4:
            letra = str(input('Digite a letra: ')).strip().lower()[0]
            for cont in range(0, len(listaAlunos)):
                if letra == listaAlunos[cont][0][0]:
                    print('=' * 30)
                    print(f'''indice: {listaAlunos[cont][3]}/ nome: {listaAlunos[cont][0]}/ idade: {listaAlunos[cont][1]}/ sexo: {listaAlunos[cont][2]}''')
                    print('=' * 30)
        elif opcao == 5:
            plt.bar([listaAlunos[cont][0] for cont in range(0, len(listaAlunos))], [listaAlunos[cont][1] for cont in range(0, len(listaAlunos))])
            plt.show()
        elif opcao == 6:
            print('=' * 30)
            print('Adicionar alunos')
            break
        elif opcao == 0:
            break
