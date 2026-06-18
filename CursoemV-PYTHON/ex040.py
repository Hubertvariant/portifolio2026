from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex040":^10}')
print('=' * 10, f'{cores[0]}')
sleep(1)

print('Leitor de média.')
nome = str(input('Média do Aluno: ')).strip().capitalize()
nota0 = float(input('Digite sua primeira nota: '))
nota1 = float(input('Digite sua segunda nota: '))
media = (nota0 + nota1) / 2

print(f'\033[1mSUA MÉDIA É {media}')
if media < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif media < 7:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')