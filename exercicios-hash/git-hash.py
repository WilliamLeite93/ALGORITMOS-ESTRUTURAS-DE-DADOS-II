import hashlib

def hash_arquivo(conteudo):
    return hashlib.sha256(conteudo.encode()).hexdigest()

def exibir_resultado(versao, conteudo):
    h = hash_arquivo(conteudo)
    print(f"\n  [ {versao} ]")
    print(f"  Conteúdo : {conteudo}")
    print(f"  Hash     : {h}")
    return h

print("Git com Hash")

v1 = "versao-1"
v2 = "versao-2"

h1 = exibir_resultado("Versão 1", v1)
h2 = exibir_resultado("Versão 2", v2)
