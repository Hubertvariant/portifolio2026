nome = str(input('Digite seu nome: ')).strip()
frase = str(input(f'{nome.capitalize()}, digite uma frase: ')).strip()
print(f'A sua frase contem {frase.lower().count("a")}')
print(f'A letra (a) aparece na frase pela primeira vez no {frase.replace(" ","").find("a") + 1}° digito, e aparece por fim no {frase.replace(" ","").rfind("a") + 1}° digito.')