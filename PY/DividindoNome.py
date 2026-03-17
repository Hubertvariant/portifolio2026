nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu ultimo nome é {nome.split()[-1]}')