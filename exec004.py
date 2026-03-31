# Simulação de Fila
# Implemente uma fila simples para processar uma sequência de nomes (entrada e
# saída), mostrando a fila a cada operação.

fila = []

while True:
    print('1 - Entrou na fila')
    print('2 - Tirar da fila')
    print('3 - Fila')
    print('4 - Sair\n')

    opcao = input('Escolha uma opção: ')

    if opcao == "1":
        nome = input('Digite seu nome: ')
        fila.append(nome)
        print(f'Fila: {fila}\n')
    elif opcao == "2":
        if fila:
            atendido = fila.pop(0)
            print(f'Atendido: {atendido}')
        else:
            print('Fila vazia\n')
        print(f'Fila: {fila}\n')

    elif opcao == "3":
        print(f'Fila: {fila}')
    
    elif opcao == "4":
        break