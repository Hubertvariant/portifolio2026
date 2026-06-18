from random import choice

# Exercício: Sorteio Simples
al1 = input('Digite o primeiro aluno: ')
al2 = input('Digite o segundo aluno:   ')
al3 = input('Digite o terceiro aluno: ')
al4 = input('Digite o quarto aluno:   ')
al5 = input('Digite o quinto aluno:   ')
al6 = input('Digite o sexto aluno:    ')
al7 = input('Digite o sétimo aluno:   ')
al8 = input('Digite o oitavo aluno:   ')
al9 = input('Digite o nono aluno:     ')
list1 = [al1, al2, al3, al4, al5, al6, al7, al8 ,al9]
escolhido = choice(list1)
print(f'O aluno sorteado para limpar o quadro foi {escolhido}')
