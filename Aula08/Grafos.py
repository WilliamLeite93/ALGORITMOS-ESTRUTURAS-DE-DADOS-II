mapa = {
    'Arad': [
        ('Zerind', 75),
        ('Sibiu', 140),
        ('Timisoara', 118)
        ],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
}

#Define as distâncias em linha reta para Bucareste (heurística).

heuristica = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374,
}

def obter_vizinhos(grafo, nodo):
    return grafo[nodo]

'''
Busca gulosa, o objetivo é encontrar o caminho do nó inicial (neste caso, Arad)
até o nó objetivo (neste caso, Bucharest).

Para isso, o algoritmo expande o nó mais promissor em cada etapa, de acordo com uma heurística,
que neste caso é a distância em linha reta até o objetivo.
'''
def busca_gulosa(mapa, heuristica, inicio, objetivo):
    # É um conjunto que armazena os nós que estão disponíveis para exploração.
    abertos = set([inicio])
    # É um conjunto que armazena os nós que já foram explorados e, portanto, não precisam mais ser avaliados.
    fechados = set([])  # Nós que já foram explorados

    caminho = {}  # Dicionário para reconstruir o caminho
    # Dicionário para acumular a distância percorrida até cada nó
    distancia_total = {
        inicio: 0
    }

    while abertos:
        nodo_atual = None
        menor_distancia = None

        '''
        Encontra o nó com a menor distância em linha reta até o objetivo
        '''
        for nodo in abertos:
            if nodo_atual is None or heuristica[nodo] < menor_distancia:
                nodo_atual = nodo
                menor_distancia = heuristica[nodo]

        if nodo_atual is None:
            return None, None

        '''
        Se o objetivo foi alcançado, reconstrói e retorna o caminho e a distância total
        '''
        if nodo_atual == objetivo:
            caminho_final = []
            while nodo_atual is not None:
                caminho_final.append(nodo_atual)
                nodo_atual = caminho.get(nodo_atual, None)
            caminho_final.reverse()
            return caminho_final, distancia_total[objetivo]

        '''
        Move o nodo atual da lista de abertos para a lista de fechados
        '''
        abertos.remove(nodo_atual)
        fechados.add(nodo_atual)

        '''
        Explora os vizinhos do nodo atual e atualiza a distância total
        '''
        for (vizinho, distancia) in obter_vizinhos(mapa, nodo_atual):
            if vizinho in fechados:
                continue
            nova_distancia = distancia_total[nodo_atual] + distancia

            if vizinho not in abertos or nova_distancia < distancia_total.get(vizinho, float('inf')):
                # get retorna o valor associado à chave especificada (vizinho, neste caso) se essa chave existir no dicionário
                # float('inf') é a representação de um infinito positivo
                abertos.add(vizinho)
                caminho[vizinho] = nodo_atual
                distancia_total[vizinho] = nova_distancia

    return None, None

'''
Executa a busca gulosa de Arad para Bucareste, retornando o caminho e a distância total
'''
caminho, distancia_total = busca_gulosa(mapa, heuristica, 'Arad', 'Bucharest')

if caminho:
    print("Caminho encontrado:", " -> ".join(caminho))
    print("Distância total percorrida:", distancia_total)
else:
    print("Caminho não encontrado")

    

def busca_a_estrela(mapa, heuristica, inicio, objetivo):
    # Guarda os nos que ainda podem ser visitados.
    abertos = set([inicio])

    # Guarda os nos que ja foram analisados.
    fechados = set([])

    # Guarda o no anterior de cada cidade para reconstruir o caminho final.
    caminho = {}

#     g(n): custo real do início até o nó
    g = {inicio: 0}

    while abertos:
#         # Seleciona o nó com o menor f(n) = g(n) + h(n)
        # No A*, f(n) = g(n) + h(n):
        # g(n) e o custo real ate o no, h(n) e a estimativa ate o objetivo.
        nodo_atual = None
        for nodo in abertos:
            if nodo_atual is None or (g[nodo] + heuristica[nodo]) < (g[nodo_atual] + heuristica[nodo_atual]):
                nodo_atual = nodo

        # Se chegamos ao objetivo, basta reconstruir e retornar o caminho.
        if nodo_atual == objetivo:
            caminho_final = []

            # Volta do objetivo ate o inicio seguindo os pais salvos em caminho.
            while nodo_atual is not None:
                caminho_final.append(nodo_atual)
                nodo_atual = caminho.get(nodo_atual, None)

            # O caminho foi montado de tras para frente, entao precisa inverter.
            caminho_final.reverse()
            return caminho_final, g[objetivo]

        # O no atual ja foi escolhido para expansao.
        abertos.remove(nodo_atual)
        fechados.add(nodo_atual)

        # Percorre os vizinhos para verificar se existe um caminho melhor ate eles.
        for vizinho, distancia in obter_vizinhos(mapa, nodo_atual):
            # Novo custo real para chegar ao vizinho passando pelo no atual.
            novo_g = g[nodo_atual] + distancia

            # Se o vizinho ja foi fechado e o novo caminho nao melhora o custo, ignora.
            if vizinho in fechados and novo_g >= g.get(vizinho, float('inf')):
                continue

            # Atualiza o vizinho quando ele ainda nao foi aberto ou quando achamos
            # um caminho com custo menor do que o registrado anteriormente.
            if vizinho not in abertos or novo_g < g.get(vizinho, float('inf')):
                caminho[vizinho] = nodo_atual
                g[vizinho] = novo_g
                abertos.add(vizinho)

    # Se todos os caminhos possiveis foram analisados e o objetivo nao apareceu.
    return None, None

caminho, distancia_total = busca_a_estrela(mapa, heuristica, 'Arad', 'Bucharest')

if caminho:
    print("Caminho encontrado com A*:", " -> ".join(caminho))
    print("Distancia total percorrida com A*:", distancia_total)
else:
    print("Caminho nao encontrado com A*")
