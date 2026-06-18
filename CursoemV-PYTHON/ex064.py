from time import sleep

print(f'\033[1;33m{'=' * 10}\n{'ex064':^10}\n{'=' * 10}\033[m')
sleep(1)

num = 0
soma = 0
tentativas = 0

num = float(input('Digite um número [999 para parar]: '))
while num != 999:
    tentativas += 1
    soma += num
    num = float(input('Digite um número [999 para parar]: '))

print(f'FIM!\nVocê digitou {tentativas} números e a soma entre eles foi {int(soma)}.')