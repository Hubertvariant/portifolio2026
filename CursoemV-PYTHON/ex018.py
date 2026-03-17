from math import radians, cos, sin, tan

# Exercício: Trigonometria
an = float(input('Digite o seu ângulo: '))
an = radians(an)
print(f'Seno de {an :>8.2f}: {sin(an):.2f}')
print(f'Cosseno de {an:>5.2f}: {cos(an):.2f}')
print(f'Tangente de {an:.2f}: {tan(an):.2f}')
