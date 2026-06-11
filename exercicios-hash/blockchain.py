import hashlib
import json

def criar_bloco(index, dados, hash_anterior):
    bloco = {
        "index": index,
        "dados": dados,
        "hash_anterior": hash_anterior,
    }
    conteudo = json.dumps(bloco, sort_keys=True)
    bloco["hash"] = hashlib.sha256(conteudo.encode()).hexdigest()
    return bloco

def exibir_bloco(bloco):
    print(f"\n  Bloco {bloco['index']}")
    print(f"  Dados          : {bloco['dados']}")
    print(f"  Hash anterior  : {bloco['hash_anterior'][:20]}...")
    print(f"  Hash atual     : {bloco['hash'][:20]}...")

def validar_cadeia(cadeia):
    print("\n  Validando cadeia...")
    valida = True
    for i in range(1, len(cadeia)):
        bloco_atual   = cadeia[i]
        bloco_anterior = cadeia[i - 1]

        # recalcula o hash do bloco anterior para comparar
        copia = {k: v for k, v in bloco_anterior.items() if k != "hash"}
        hash_recalculado = hashlib.sha256(json.dumps(copia, sort_keys=True).encode()).hexdigest()

        encadeado = bloco_atual["hash_anterior"] == bloco_anterior["hash"]
        integro   = hash_recalculado == bloco_anterior["hash"]

        if encadeado and integro:
            print(f"  ✓ Bloco {i}: hash anterior confere com o Bloco {i - 1}")
        else:
            print(f"  ✗ Bloco {i}: QUEBRADO — Bloco {i - 1} foi adulterado!")
            valida = False

    if valida:
        print("  → Cadeia íntegra.\n")
    else:
        print("  → Cadeia corrompida!\n")

# ── Criando os três blocos ──────────────────────────────────────────
print("\n" + "=" * 52)
print("       DEMO — Blockchain Simplificada")
print("=" * 52)

bloco0 = criar_bloco(0, "Genesis",                    "0" * 64)
bloco1 = criar_bloco(1, "Alice envia 50 BTC a Bob",   bloco0["hash"])
bloco2 = criar_bloco(2, "Bob envia 20 BTC a Carol",   bloco1["hash"])

cadeia = [bloco0, bloco1, bloco2]

print("\n  ── Cadeia original ──")
for bloco in cadeia:
    exibir_bloco(bloco)

validar_cadeia(cadeia)

# ── Adulterando o Bloco 0 ───────────────────────────────────────────
input("  Pressione Enter para adulterar o Bloco 0...")

print("\n  ── Adulterando Bloco 0: alterando os dados sem recalcular o hash ──")
cadeia[0]["dados"] = "Genesis ADULTERADO"

for bloco in cadeia:
    exibir_bloco(bloco)

validar_cadeia(cadeia)