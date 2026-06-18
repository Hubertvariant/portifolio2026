#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Usuario digitar 7 valores numericos em uma lista unica
valores = [[],[]]
for i in range(0,7):
    while True:
        try:
            numero = int(input(f"Digite {i+1}° valor: "))
            break
        except ValueError:
            print("caractere invalido! tente novamente")

    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
    
print(f"Os valores digitados pares foram:\n{sorted(valores[0])}")
print(f"Os valores digitados impares foram:\n{sorted(valores[1])}")