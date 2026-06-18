from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"83":=^40}\033[m')
print('Validando expressões numéricas')

expressao = str(input('Digite uma expressão: ')).strip()
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print(f'A expressão {expressao} é válida!')
else:
    print(f'A expressão {expressao} NÃO é válida!')