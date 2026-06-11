import hashlib
import os

def gerar_hash(senha):
    salt = os.urandom(16).hex()
    hash_senha = hashlib.sha256((salt + senha).encode()).hexdigest()
    return salt, hash_senha

def fazer_login(banco, usuario, senha):
    if usuario not in banco:
        return False
    registro = banco[usuario]
    hash_tentativa = hashlib.sha256((registro["salt"] + senha).encode()).hexdigest()
    return hash_tentativa == registro["hash"]

USUARIO = "william"
SENHA   = "senha123"

banco = {}

print("\n  CADASTRO")
print(f"  Usuário  : {USUARIO}")
print(f"  Senha    : {SENHA}")

salt, hash_senha = gerar_hash(SENHA)
banco[USUARIO] = {"salt": salt, "hash": hash_senha}

print(f"\n  Salt gerado : {salt}")
print(f"  Hash salvo  : {hash_senha}")

print("\n  " + "─" * 48)
print("\n  Teste Login - senha correta")

hash_tentativa = hashlib.sha256((banco[USUARIO]["salt"] + SENHA).encode()).hexdigest()
if fazer_login(banco, USUARIO, SENHA):
    print("  ✓ Login bem-sucedido!")

print(f"\n  Hash calculado : {hash_tentativa}")
print(f"  Hash no banco  : {banco[USUARIO]['hash']}")


SENHA_ERRADA = "senhaerrada"

print("\n  " + "─" * 48)
print("\n  Teste Login — senha incorreta")
print(f"  Usuário  : {USUARIO}")
print(f"  Senha    : {SENHA_ERRADA}")

hash_errado = hashlib.sha256((banco[USUARIO]["salt"] + SENHA_ERRADA).encode()).hexdigest()
print(f"\n  Hash calculado : {hash_errado}")
print(f"  Hash no banco  : {banco[USUARIO]['hash']}")

if not fazer_login(banco, USUARIO, SENHA_ERRADA):
    print("  ✗ Senha incorreta — hashes não conferem.")
