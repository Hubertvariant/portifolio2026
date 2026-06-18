import random

listaAluno = []

for i in range(0,4):
    aluno = str(input(f'Digite o nome do aluno representante do {i + 1}° grupo: ')).strip().capitalize()
    if aluno in listaAluno:
        print('Aluno já está cadastrado')
    else:
        listaAluno.append(aluno)

random.shuffle(listaAluno)
print('A ordem de apresentação será:', listaAluno)