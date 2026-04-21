vetor = [1, 1, 1, 2, 3, 3]

def removerDuplicatas(vetor):
    indice = 1

    for i in range(1, len(vetor)):
        if vetor[i] != vetor[i - 1]:
            vetor[indice] = vetor[i]
            indice += 1
    return(vetor[:indice])

resultado = removerDuplicatas(vetor)
print(resultado)