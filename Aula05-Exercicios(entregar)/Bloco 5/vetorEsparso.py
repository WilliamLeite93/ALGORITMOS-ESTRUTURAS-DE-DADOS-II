vetor = [0]*40 + [1,2,3,4,5,6,7,8,9,10]

def vetorEsparso(vetor):
   contador = 0

   for i in range(len(vetor)):
      if vetor[i] == 0:
        contador += 1
   limite = 50 * 0.7
   if contador > limite:
        print("Vetor Ineficiente: Recomenda-se compressão")
   else:
        print(f"Os zeros correspondem a menos que 70% do vetor")
vetorEsparso(vetor)
