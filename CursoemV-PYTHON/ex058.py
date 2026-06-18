from random import randint
from time import sleep

print(f'\033[1;33m{'=' * 10}\n{'ex058':^10}\n{'=' * 10}\033[m')
sleep(1)

print('\033[1;33mJogo\033[m \033[1mde \033[1;34madivinhação\033[m \033[1mV2.0 \nIrei pensar em um número entre 0 e 10 \nTente adivinhar')
sleep(1)
print('\033[37mpensando...\033[m\033[1m')
sleep(3)

compNum = randint(0, 10)
palpite = int(input('Qual é o seu palpite? '))
numPalpites = 1

while palpite != compNum:
    if compNum > palpite:
        print('Mais...')
    else:
        print('Menor...')
    
    palpite = int(input('\033[31;1mVocê errou!!\033[m\n\033[1mTente novamente: '))
    numPalpites += 1

print(f'\033[32;1mParabens!!\033[m \033[1mvocê \033[32;1macertou!!\033[m\n\033[1mPrecisou de {numPalpites} palpites para acertar')