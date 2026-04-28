valores = [10,5,2,7,15,12,20]

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def inserir(raiz, valor):
    if raiz is None:
        return Node(valor)
    if valor < raiz.valor:
        raiz.esq = inserir(raiz.esq, valor)
    else:
        raiz.dir = inserir(raiz.dir, valor)
    return raiz

def pre_ordem(raiz):
    if raiz is None:
        return
    print(raiz.valor, end=" ")
    pre_ordem(raiz.esq)
    pre_ordem(raiz.dir)

def pos_ordem(raiz):
    if raiz is None:
        return
    pos_ordem(raiz.esq)
    pos_ordem(raiz.dir)
    print(raiz.valor, end=" ")

def in_ordem(raiz):
    if raiz is None:
        return
    in_ordem(raiz.esq)
    print(raiz.valor, end=" ")
    in_ordem(raiz.dir)   

tree = None

for valor in valores:
    tree = inserir(tree, valor)

print("Pré Ordem")
pre_ordem(tree)
print()
print("Pós Ordem:")
pos_ordem(tree)
print()
print("Em ordem:")
in_ordem(tree)
