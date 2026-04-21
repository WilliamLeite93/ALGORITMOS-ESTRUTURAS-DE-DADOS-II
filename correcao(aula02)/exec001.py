# 1) Contar Dígitos Pares

# Ideia:
# Percorrer cada dígito do número e verificar se ele é par.

def contar_digitos_pares(numero: int) -> int:
    numero_texto = str(abs(numero))
    quantidade_pares = 0

    for digito in numero_texto:
        if int(digito) % 2 == 0:
            quantidade_pares += 1

    return quantidade_pares


# Exemplo de uso
numero = 248531
resultado = contar_digitos_pares(numero)
print(f"Quantidade de dígitos pares: {resultado}")