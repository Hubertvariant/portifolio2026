print('Menu de atividades')
print('1) Tinta para parede')
print('2) Desconto de 5%')
print('3) Conversão de Temperaturas')
ex = int(input('Digite uma opção: '))

if ex == 1:
    print('1) Tinta para parede')
    lar = float(input('Digite a largura da parede: '))
    alt = float(input('Digite a altura da parede: '))
    area = lar * alt
    print(f'Para pintar uma parede de {lar} x {alt} que possui {area}m2 voce precisara de {alt / 2} litros de tinta')

elif ex == 2:
    print('2) Desconto de 5%')
    prod = int(input('Digite o valor do produto: '))
    print(f'O valor do produto com 5% de desconto é: {prod / 100 * 5}')

elif ex == 3:
    print('3) Conversão de Temperaturas')
    c = float(input('Digite a temperatura em Celsius: '))
    f = c * 1.8 + 32
    print(f'{c}°C corresponde a {f}°F')