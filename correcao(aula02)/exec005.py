# 5) Remover Elementos Negativos de Lista

# Ideia:
# Criar uma nova lista apenas com os valores maiores ou iguais a zero.

def remover_negativos(lista_numeros: list[int]) -> list[int]:
    nova_lista = []

    for numero in lista_numeros:
        if numero >= 0:
            nova_lista.append(numero)

    return nova_lista


# Exemplo de uso
numeros = [10, -3, 7, -1, 0, 25, -8]
resultado = remover_negativos(numeros)
print(resultado)