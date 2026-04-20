vetor = ["Matheus", "Igor", "Pedro", "Ana"] + [None] * 6

def inserirNoInicio(vetor, novoPaciente):
    movimentos = 0
    for i in range(9, 0, -1):
        vetor[i] = vetor[i - 1]
        movimentos += 1
    vetor[0] = novoPaciente
    return vetor, movimentos

print(f'Vetor inicial - {vetor}')
vetor, movimentos = inserirNoInicio(vetor, "Henrique")
print(f'Após Adição - {vetor}')
print(f'Custo de Memória: {movimentos} movimentos')



def removerDaPosicao(vetor, indice):
    movimentos = 0
    for i in range(indice, 9):
        vetor[i] = vetor[i + 1]
        movimentos += 1
    vetor[9] = None
    return vetor, movimentos
print()
vetor, movimentos = removerDaPosicao(vetor, 1)
print(f'Remoção no índice específico : {vetor}')
print(f'Custo de Memória: {movimentos} movimentos')

vetor[4] = "Fernanda"
print()
print(f'Adição no final do vetor - {vetor}')
print(f'Inserção no final custa 0 movimentos')
