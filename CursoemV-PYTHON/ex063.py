from time import sleep

print(f'\033[1;34m{'=' * 10}\n{'ex063':^10}\n{'=' * 10}\033[m')
sleep(1)

print('Fibonacci series')
n = int(input('Digite quantos termos você quer mostrar: '))

f1 = 0
f2 = 1
print(f'{f1} -> {f2}', end='')
cont = 3
while cont <= n:
    f3 = f1 + f2
    print(f' -> {f3}', end='')
    f1 = f2
    f2 = f3
    cont += 1
print(' -> FIM')