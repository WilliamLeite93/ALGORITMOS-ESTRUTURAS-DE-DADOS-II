vetor = [None] * 5

def inserirElementos(vetor):
    contador = 0
    for i in range(21):
        if contador >= len(vetor):
            print(f"\n--- OVERFLOW NO ITEM {i}! ---")
            vetor = vetor + ([None] * len(vetor))
            print(f"Nova Capacidade Real: {len(vetor)}")
        
        vetor[contador] = i
        contador += 1

        print(f"Itens: {contador:2} | Capacidade Real: {len(vetor):2}")
    
    return vetor

vetor = inserirElementos(vetor)
print("\nVetor final:", vetor)