# 4) Simulação de Fila

# Ideia:
# Fila funciona no modelo FIFO:
# Primeiro que entra, primeiro que sai.

def mostrar_fila(fila: list) -> None:
    print("Fila atual:", fila)


def enfileirar(fila: list, nome: str) -> None:
    fila.append(nome)
    print(f"{nome} entrou na fila.")
    mostrar_fila(fila)


def desenfileirar(fila: list) -> None:
    if len(fila) == 0:
        print("A fila está vazia.")
        return

    nome_removido = fila.pop(0)
    print(f"{nome_removido} saiu da fila.")
    mostrar_fila(fila)


# Exemplo de uso
fila_nomes = []

enfileirar(fila_nomes, "Pablo")
enfileirar(fila_nomes, "Bruna")
enfileirar(fila_nomes, "Gladimir")

desenfileirar(fila_nomes)
desenfileirar(fila_nomes)