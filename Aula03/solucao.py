def gerar_condicoes(condicoes: list[str]) -> list[dict]:
    casos = [{}]
    
    for condicao in condicoes:
        novos_casos = []
        for caso in casos:
         
            novos_casos.append({**caso, condicao: True}) # spread operator para manter as chaves e valores do dicionário 'caso' e adicionar a nova chave 'condicao' com o valor True
            
            novos_casos.append({**caso, condicao: False})
        casos = novos_casos 
    return casos

condicoes = [
    "Usuário possui cadastro?"
]


casos = gerar_condicoes(condicoes)

print(f"Total de casos: {len(casos)}")
print("\nCasos gerados:")
for caso in casos:
    print(caso)


