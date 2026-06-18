cit = str(input('Digite o nome da sua cidade: ')).strip()
div2 = cit.split()
resultado = 'santo' in div2[0].lower()
print('A cidade começa com o nome Santo:', resultado)