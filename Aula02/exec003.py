
# Reversão com Pilha
# Usando a estrutura de pilha, crie uma função que inverta uma palavra digitada pelo
# usuário.

palavra = input('Digite a palavra a ser invertida: ')

resultado = ""
pilha = []

for i in palavra:
    pilha.append(i)
while pilha:
    letra = pilha.pop()
    resultado = resultado + letra

print(f'Palavra invertida: {resultado}')