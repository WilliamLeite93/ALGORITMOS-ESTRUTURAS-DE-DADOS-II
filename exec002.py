# Substituição de Caracteres em String
# Implemente uma função que recebe uma string e retorna a mesma string com todas
# as vogais substituídas por ‘*’.

palavra = input('Digite uma palavra: ').lower()

resultado = ""

vogais = ["a", "e", "i", "o", "u", "y"]

for i in palavra:
    if i in vogais:
        resultado = resultado + "*"
    else:
        resultado = resultado + i

print(f'Palavra: {resultado}')