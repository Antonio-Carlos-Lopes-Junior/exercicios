"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso
ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
try:
    altura = float(input('Digite sua altura em metros: '))
except ValueError:
    print('Você não digitou um número.')
else:
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso:.3f} Kg')
