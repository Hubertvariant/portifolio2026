
n = int(input('Digite um número: '))
print(f'O sucessor de {n} é {n + 1} e o antecessor é {n - 1}')


print(f'O dobro de {n} é {n ** 2}',end=', ')
print(f'o triplo é {n ** 3}', end=', ')
print(f'a raizQ é {n ** (1 / 2)}.')


nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a sua nota de matemática: '))
n2 = float(input('Digite a sua nota de portugues: '))
print(f'a média das notas do aluno {nome} é {(n1 + n2) / 2}.')


metros = float(input('Digite um valor em metros: '))
print(f'O seu valor em metros para centimetros é {metros * 100}, e em milimetros é {metros * 1000}')


tab = int(input('Digite um valor para a tabuada: '))
print(f'{tab} x 1 = {tab * 1}')
print(f'{tab} x 2 = {tab * 2}')
print(f'{tab} x 3 = {tab * 3}')
print(f'{tab} x 4 = {tab * 4}')
print(f'{tab} x 5 = {tab * 5}')
print(f'{tab} x 6 = {tab * 6}')
print(f'{tab} x 7 = {tab * 7}')
print(f'{tab} x 8 = {tab * 8}')
print(f'{tab} x 9 = {tab * 9}')
print(f'{tab} x 10 = {tab * 10}')


din = float(input('Digite quantos reais deseja converter para dolar: '))
print(f'A conversão de R${din} para dolar: ${din/5.42}')


l1 = float(input('Digite a altura da sua parede: '))
l2 = float(input('Digite a largura da sua parede: '))
print(f'A área da sua parede é {l1 * l2}, para pintar a parede é será necessario {l1 * l2 // 2 + 1}')


preco = float(input('Qual o preço do produto: R$'))
print(f'Preço com 5% de desconto: R${preco - preco * 5 / 100 :2}')


sal = float(input('Digite o seu salário: R$'))
print(f'O seu salario {nome} recebeu um aumento de 15% que é igual a R${sal + sal * 15 / 100 :2}')


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


km = float(input('Quantos quilometros você rodou? '))
dias = int(input('Quantos dias vc ficou com o carro? '))
dias = dias * 60
km = km * 0.15
print(f'O valor a pagar é {dias:.2f} dias e {km:.2f} por Km rodade {dias + km:.2f}')
