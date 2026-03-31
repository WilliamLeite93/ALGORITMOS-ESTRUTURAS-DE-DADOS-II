import random

valores = [random.randint(0, 200) for _ in range(100)]

if 25 in valores:
    print('O numero 25 está no array')
else: 
    print('O numero 25 não está no array')
    
# o pior caso é O(n) porque o valor pode estar na ultima posição
# ou pior, nem estar lá e mesmo assim ele terá que percorrer o array
#todo para ter certeza
