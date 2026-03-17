from math import factorial
from time import sleep

print(f'\033[1;34m{'=' * 10}\n{'ex060':^10}\n{'=' * 10}\033[m')
sleep(1)

print('\033[1;33mFATORIAL!\033[m\033[1m')
n = int(input('Digite um número para o calculo do fatorial: '))

fat = factorial(n)
c = n

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1

print(fat)
sleep(1)