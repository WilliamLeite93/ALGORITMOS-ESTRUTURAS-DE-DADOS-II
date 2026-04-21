# 3) Reversão com Pilha

# Ideia:
# Usar uma lista como pilha:
# append() para empilhar
# pop() para desempilhar

def inverter_palavra_com_pilha(palavra: str) -> str:
    pilha = []

    for letra in palavra:
        pilha.append(letra)

    palavra_invertida = ""

    while pilha:
        palavra_invertida += pilha.pop()

    return palavra_invertida


# Exemplo de uso
palavra = "python"
resultado = inverter_palavra_com_pilha(palavra)
print(resultado)