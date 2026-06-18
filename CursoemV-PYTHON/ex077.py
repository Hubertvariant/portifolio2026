from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"077":=^40}\033[m')
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {cor[randint(0, 1)]}{p.upper()}\033[m temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print()