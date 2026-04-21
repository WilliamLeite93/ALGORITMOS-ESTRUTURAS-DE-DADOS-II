# 7) Contagem de Palavras em String

# Ideia:
# Separar a frase em palavras e contar quantas vezes cada uma aparece.

def contar_palavras(frase: str) -> dict[str, int]:
    palavras = frase.lower().split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem


# Exemplo de uso
frase = "Bem Legal aprender algoritmos"
resultado = contar_palavras(frase)
print(resultado)