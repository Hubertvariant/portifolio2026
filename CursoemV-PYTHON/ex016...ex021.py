from math import sqrt, radians ,cos, sin , tan
from random import choice, shuffle
import pygame
from time import sleep
pygame.init()
n = float(input('digite um número real: '))
print(f'O número {n} tem a parte inteira {int(n)}')


co = int(input('Cateto oposto: '))
ca = int(input('Cateto adjacente: '))
hip = co ** 2 + ca ** 2
print(f'O comprimento da hipotenusa: {int(sqrt(hip))}')


an = float(input('Digite o seu ângulo: '))
an = radians(an)
print(f'Seno de {an :>8.2f}: {sin(an):.2f}')
print(f'Cosseno de {an:>5.2f}: {cos(an):.2f}')
print(f'Tangente de {an:.2f}: {tan(an):.2f}')


al1 = input('Digite o primeiro aluno: ')
al2 = input('Digite o segundo aluno:  ')
al3 = input('Digite o terceiro aluno: ')
al4 = input('Digite o quarto aluno:   ')
al5 = input('Digite o quinto aluno:   ')
al6 = input('Digite o sexto aluno:    ')
al7 = input('Digite o sétimo aluno:   ')
al8 = input('Digite o oitavo aluno:   ')
al9 = input('Digite o nono aluno:     ')
list1 = [al1, al2, al3, al4, al5, al6, al7, al8 ,al9]
escolhido = choice(list1)
print(f'O aluno sorteado para limpar o quadro foi {escolhido}')


#Alunos do ex passado //
list2 = [al1, al2, al3, al4]
shuffle(list2)
print(f'A ordem de apresentação será: {list2}')


pygame.mixer.init()
pygame.mixer.music.load('lestGo.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)