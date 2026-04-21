vetor = [50, 100, 150, 200, 210, 220, 230, 240, 250]

def encontrarValor(vetor):
    largura = 3
    for linha in range(0, 3):
        for coluna in range(0, 3):
            indice = linha * largura + coluna
            valor = vetor[indice]
            print(f"L:{linha} C:{coluna} -> índice:{indice} valor:{valor}")

encontrarValor(vetor)

def filtroContraste(vetor):
    for i in range(len(vetor)):
        valor = vetor[i]
        novo_valor = round(valor * 1.2)

        if novo_valor > 255:
            novo_valor = 255

        vetor[i] = novo_valor

filtroContraste(vetor)
print()
print(vetor)

def inversao(vetor):
  inicio = 0
  fim = len(vetor) - 1

  while inicio < fim:
      aux = vetor[inicio]
      vetor[inicio] = vetor[fim]
      vetor [fim] = aux

      inicio = inicio + 1
      fim = fim - 1

inversao(vetor)
print()
print(vetor)