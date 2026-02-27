print('Menu de atividades')
print('1) Tinta para parede')
print('2) Desconto de 5%')
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

