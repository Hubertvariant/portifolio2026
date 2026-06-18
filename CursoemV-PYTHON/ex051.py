from time import sleep

print(f'''\033[33;1m{"=" * 10}
{"ex051":^10}
{"=" * 10}\033[m''')
sleep(1)

p1 = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = p1 + (10 - 1) * razão

for c in range(p1, décimo + razão, razão):
    print(c, end=' -> ')
print('Acabou!')