from math import sqrt

print('====== 17 ======')

co = int(input('Cateto oposto: '))
ca = int(input('Cateto adjacente: '))
hip = co ** 2 + ca ** 2
print(f'O comprimento da hipotenusa: {int(sqrt(hip))}')