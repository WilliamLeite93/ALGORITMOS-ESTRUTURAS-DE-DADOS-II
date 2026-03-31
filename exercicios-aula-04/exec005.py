
numeros = [10, 20, 30, 40, 50]

def mostrar_primeiro_numero():
    print("Primeiro número:", numeros[0])

def mostrar_ultimo_numero():
    print("Último número:", numeros[-1])

def somar_numeros():
    soma = sum(numeros)
    print("Soma dos números:", soma)

def buscar_valor():
    if 10 in numeros:
        print("O valor 10 está presente na lista.")
    else:
        print("O valor 10 não está presente na lista.")


mostrar_primeiro_numero()
mostrar_ultimo_numero()
somar_numeros()
buscar_valor()
