# 2) Substituição de Caracteres em String

# Ideia:
# Percorrer a string e trocar toda vogal por *.

def substituir_vogais_por_asterisco(texto: str) -> str:
    vogais = "aeiouAEIOU"
    novo_texto = ""

    for caractere in texto:
        if caractere in vogais:
            novo_texto += "*"
        else:
            novo_texto += caractere

    return novo_texto


# Exemplo de uso
frase = "Algoritmos e Estruturas"
resultado = substituir_vogais_por_asterisco(frase)
print(resultado)