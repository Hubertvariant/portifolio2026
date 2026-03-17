nome = str(input('Digite seu nome completo: ')).strip()
maius = nome.upper()
minus= nome.lower()
totalLetras = len(nome) - nome.count(' ')
print(f'''O nome em maiusculas: {maius}
O nome em minusculas: {minus}
Total de letras: {totalLetras}''')
nomeLista = nome.split()
for letra in nomeLista:
    print(f'A primeira letra do nome {letra} é: {letra[0]} e o total de letras é: {len(letra)}')
