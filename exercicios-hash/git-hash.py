import hashlib

def simular_commit(nome_arquivo, conteudo):
    hash_resultado = hashlib.sha256(conteudo.encode()).hexdigest()
    
    print(f" Arquivo : {nome_arquivo}")
    print(f" Conteúdo: '{conteudo}'")
    print(f" Git Hash: {hash_resultado}")
    return hash_resultado

print("\n" + "=" * 60)
print("  SIMULAÇÃO DE COMMIT GIT")

config_original = "acesso=user;porta=8080;debug=false;"
print("\n COMMIT 1: Configuração Padrão ")
hash1 = simular_commit("config.env", config_original)

config_alterada = "acesso=admin;porta=8080;debug=false;"
print("\n COMMIT 2: Alteração de Acesso")
hash2 = simular_commit("config.env", config_alterada)

print("\n" + "-" * 60)
print("  DIFERENÇAS ENTRE HASHES:")
print(f"  Hash 1: {hash1}")
print(f"  Hash 2: {hash2}")
print("-" * 60)