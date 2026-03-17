from datetime import date

c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print(f'{c[1]}=' * 20)
print(f'{c[2]}ex032')
print(f'{c[1]}={c[0]}' * 20)

ano = str(input('Em que ano você está EX[9999]? '))
if ano == '0' or ano == '':
    ano = date.today().year
else:
    ano = int(ano)

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} {c[4]}é bissexto!')
else:
    print(f'{ano} {c[5]}não é bissexto!')