from random import choices

listaAlunos = list()

cont = 0
while True:
    if cont == 4:
        break
    nome = str(input('Digite seu nome: ')).strip().lower()
    if nome in listaAlunos:
        print('Nome ja cadastrado')
    else:
        listaAlunos.append(nome)
        cont += 1
        
sorteado = choices(listaAlunos)
print('O aluno que ira apagar o quadro será', sorteado.capitalize())
