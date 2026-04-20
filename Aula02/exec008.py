
lista_telefones = {
    'João': '1234-5678',
    'Maria': '9876-5432',
    'Pedro': '5555-5555',
    'Ana': '1111-1111'
}

def buscar_telefone(lista_telefones: dict[str, str], nome: str) -> str:
    if nome in lista_telefones:
        return lista_telefones[nome]
    return "Contato não encontrado."


def listar_contatos_ordenados(lista_telefones: dict[str, str]) -> None:
    for nome in sorted(lista_telefones.keys()):
        print(f"{nome}: {lista_telefones[nome]}")


print(buscar_telefone(lista_telefones, "Maria"))
print(buscar_telefone(lista_telefones, "Carlos"))

print("\nContatos em ordem alfabética:")
listar_contatos_ordenados(lista_telefones)