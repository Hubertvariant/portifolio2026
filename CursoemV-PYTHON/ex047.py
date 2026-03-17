from time import sleep

print('\033[33;1m=' * 10)
print(f'{"ex047":^10}')
print('=' * 10, '\033[m')
sleep(1)

print('\033[1mNÚMEROS PARES!\033[m')
sleep(1)
for c in range(2, 51, 2):
    print(f'{c}...', end=' ')
print('\033[1mFIM!\033[m')