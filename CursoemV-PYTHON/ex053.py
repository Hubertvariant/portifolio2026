print('\033[33;1m=' * 10)
print(f'{"ex053":^10}')
print('=' * 10, '\033[m')

print('\033[1mReconhecedor de polindromo')
frase = str(input('Digite uma frase: ')).replace(' ', '').lower()
print(f'\033[1mO inverso da palavra {frase} é {frase[::-1]}\033[m\033[1m')

if frase[::-1] == frase:
    print('Essa frase é um \033[36;1mpolidromo\033[m!')
else:
    print('Essa frase \033[31;1mnão\033[m \033[1mé um \033[36;1mpolidromo\033[m!')