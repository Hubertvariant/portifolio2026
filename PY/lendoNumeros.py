num = int(input('Digite um número 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')