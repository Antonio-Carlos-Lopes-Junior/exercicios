"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
lista = []
num = 0
soma = 0
while True:
    try:
        num = int(input('Digite um número: '))
    except ValueError:
        print('Digite um número')
    else:
        lista.append(num)
        soma += num
        print('Quer incluir mais número?')
        while True:
            mais_numero = input('Digite S - Sim ou N - Não: ').upper()

            if mais_numero != 'N' and mais_numero != 'S':
                print('Você não digitou S - Sim ou N - Não')
            else:
                break
        if mais_numero == 'N':
            lista.sort()
            print(f'O menor número é: {lista[0]}')
            print(f'O maior número é: {lista[len(lista) - 1]}')
            print(f'A soma é: {soma}')
            break
