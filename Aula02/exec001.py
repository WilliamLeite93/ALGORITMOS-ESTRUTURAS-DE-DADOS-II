# Contar Dígitos Pares
# Escreva um algoritmo que, dado um número inteiro, retorna a quantidade de dígitos
# pares existentes nele.

numero = input('Digite um número: ')

resultado = 0

for i in numero:
    if int(i) % 2 == 0:
        resultado = resultado + 1

print(f'Os números pares aparecem {resultado} vezes')