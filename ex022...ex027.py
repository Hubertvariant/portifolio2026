import pygame
from time import sleep
pygame.init()
nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome em maiusculo: {nome.upper()}')
print(f'Seu nome em minusculo: {nome.lower()}')
print(f'Número de letras do seu nome: {len(nome.replace(' ',''))}')
div = nome.split()
print(f'Número de letras do primeiro nome: {len(div[0])}')


print('Seu nome tem o nome Silva: ', 'silva' in nome.lower())


n = int(input('Digite um número de até 4 digitos EX[9999]: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando{n}...')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')


cont = len(div)
print(f'Seu primeiro nome: {div[0]}')
print(f'Seu ultimo nome: {div[cont - 1]}')


cit = str(input('Digite o nome da sua cidade: ')).strip()
div2 = cit.split()
cit = 'santo' in div2[0].lower()
print('A cidade começa com o nome Santo:',cit)


frase = str(input(f'{nome.capitalize()}, digite uma frase: ')).strip()
print(f'A sua frase contem {frase.lower().count('a')}')
print(f'A letra (a) aparece na frase pela primeira vez no {frase.replace(' ','').find('a') + 1}° digito, e aparece por fim no {frase.replace(' ','').rfind('a') + 1}° digito.')


pygame.mixer.init()
pygame.mixer.music.load('lestGo.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)