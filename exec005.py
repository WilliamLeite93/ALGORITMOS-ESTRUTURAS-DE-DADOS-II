# Remover Elementos Negativos de Lista
# Dado um vetor/lista de inteiros, escreva um algoritmo que retorna uma nova lista
# apenas com os números não-negativos.

lista_numeros = [8, -3, 5, -1, 0, 4, -5, -7]

nao_negativos = []

for i in lista_numeros:
    if i >= 0:
        nao_negativos.append(i)
print(f'Nova lista: {nao_negativos}')
