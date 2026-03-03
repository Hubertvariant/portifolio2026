print('====== 14 ======')

print('Tá calor ai? Quer saber a temperatura?')
res = str(input('Onde você tá está como C° ou F° EX[C/F]: ')).strip().upper()
if res == 'C':
    c = float(input('Digite a temperatura em C°: '))
    f = 9 * c / 5 + 32
    tem = {0: 'C°', 1: c, 2: 'F°',3:f}
elif res == 'F':
    f = float(input('Digite a temperatura em F°: '))
    c = (f - 32) * 5 / 9
    tem = {0: 'F°', 1: f, 2: 'C°',3:c}
else:
    print('impossivel calcular')
print(f'A conversão de {tem[1]}{tem[0]} é igual a {tem[3]:.2f}{tem[2]}')
