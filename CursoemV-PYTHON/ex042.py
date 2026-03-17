from time import sleep

cores = {0: '\033[m', 1: '\033[31;1m'}

print(f'{cores[1]}=' * 10)
print(f'{"ex042":^10}')
print('=' * 10, f'{cores[0]}')

print('\033[1mTRIÂNGULOS\033[m')
al = float(input('\033[33mQual o tamanho da reta a? '))
bl = float(input('\033[32mQual o tamanho da reta b? '))
cl = float(input('\033[36mQual o tamanho da reta c? \033[m'))
sleep(1)

if al < bl + cl and bl < cl + al and cl < al + bl:
    print('\033[33;1mÉ possivel montar um triangulo!\033[m\033[1;36m', end=' ')
    if al == bl == cl:
        print('Equilatero!', end='')
    elif al != bl != cl != al:
        print('Escaleno!', end='')
    else:
        print('Isosceles!', end='')
    print('\033[m')
else:
    print('\033[31;1mNÃO\033[m \033[1mé possivel montar um triângulo!\033[m')