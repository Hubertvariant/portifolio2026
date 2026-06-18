c = {0: '\033[m', 1: '\033[36m', 2: '\033[33m', 4: '\033[32m', 5:'\033[31m'}

print('=' * 20)
print('ex035')
print('=' * 20)

aL = float(input(f'{c[2]}Digite o primeiro lado do triângulo: '))
bL = float(input(f'{c[1]}Digite o segundo lado do triângulo: '))
cL = float(input(f'{c[4]}Digite o terceiro lado do triângulo: '))

if aL < bL + cL and bL < aL + cL and cL < aL + bL:
    print(f'{c[0]}As retas {c[2]}a:{aL}{c[0]}, {c[1]}b:{bL}{c[0]} e {c[4]}c:{cL}{c[0]} podem forma um triângulo!')
else:
    print(f'{c[0]}As retas {c[2]}a:{aL}{c[0]}, {c[1]}b:{bL}{c[0]} e {c[4]}c:{cL}{c[0]} {c[5]}não podem{c[0]} forma um triângulo!')