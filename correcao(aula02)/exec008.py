# 8) Busca em Dicionário de Contatos

# Ideia:
# Usar um dicionário no formato:
# chave = nome
# valor = telefone

def buscar_telefone(contatos: dict[str, str], nome: str) -> str:
    if nome in contatos:
        return contatos[nome]
    return "Contato não encontrado."


def listar_contatos_ordenados(contatos: dict[str, str]) -> None:
    for nome in sorted(contatos.keys()):
        print(f"{nome}: {contatos[nome]}")


# Exemplo de uso
contatos = {
    "Edecio": "99999-1111",
    "Angelo": "98888-2222",
    "Wagner": "97777-3333"
}

print(buscar_telefone(contatos, "Angelo"))
print(buscar_telefone(contatos, "Pablo"))

print("\nContatos em ordem alfabética:")
listar_contatos_ordenados(contatos)