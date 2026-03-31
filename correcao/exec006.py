# 6) Remover Duplicatas Usando Conjunto

# Ideia:
# O set não permite valores repetidos.

def remover_duplicatas_preservando_ordem(lista_numeros: list[int]) -> list[int]:
    numeros_vistos = set()
    nova_lista = []

    for numero in lista_numeros:
        if numero not in numeros_vistos:
            numeros_vistos.add(numero)
            nova_lista.append(numero)

    return nova_lista


# Exemplo de uso
numeros = [1, 2, 2, 3, 4, 4, 5, 1]
resultado = remover_duplicatas_preservando_ordem(numeros)
print(resultado)