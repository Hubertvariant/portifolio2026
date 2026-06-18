from random import randint

contCor = randint(0, 1)
cor = ('\033[1;36m', '\033[1;33m')

print(f'{cor[contCor]}{"072":=^40}\033[m')
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = input('Digite um número de 0 a 20: ')
    if numero.isnumeric():
        numero = int(numero)
        if 0 <= numero <= 20:
            break
    print('Tente novamente! ', end='')

print(f'O número {numero} em extenso é: {extenso[numero]}')