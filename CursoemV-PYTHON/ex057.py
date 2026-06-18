from time import sleep

print(f'''\033[1;33m{'=' * 10}
{'ex057':^10}
{'=' * 10}\033[m''')
sleep(1)

print('\033[1;34mVerificador\033[m \033[1mde \033[1;33mDados\033[m')
sexo = str(input('\033[1mDigite seu sexo: \033[m')).strip()

while sexo not in 'MmFf':
    print('\033[1;31m[ERRO!]\033[m')
    sexo = str(input('\033[1mDigite seu sexo novamente: \033[m')).upper().strip()

print(f'Sexo {sexo.upper()} registrado com sucesso!')