import hashlib
import json

def registrar_etapa(id_lote, status, hash_anterior):
    dados_etapa = {
        "id_lote": id_lote,
        "data_hora": "2026-06-15 12:00:00",
        "status": status
    }
 
    bloco = {
        "dados": dados_etapa,
        "hash_anterior": hash_anterior
    }
    
    conteudo_json = json.dumps(bloco, sort_keys=True)
    bloco["hash_atual"] = hashlib.sha256(conteudo_json.encode()).hexdigest()
    
    return bloco

def exibir_historico(cadeia):
    for i, bloco in enumerate(cadeia):
        print(f"\n [Bloco {i}]") 
        print(f"  Status        : {bloco['dados']['status']}")
        print(f"  Hash Anterior : {bloco['hash_anterior'][:20]}...")
        print(f"  Hash Atual    : {bloco['hash_atual'][:20]}...")

def validar_cadeia(cadeia):
    print("\n [ AUDITORIA...]")
    cadeia_valida = True
    
    for i in range(1, len(cadeia)):
        bloco_atual = cadeia[i]
        bloco_anterior = cadeia[i - 1]
        
        copia_anterior = {k: v for k, v in bloco_anterior.items() if k != "hash_atual"}
        json_anterior = json.dumps(copia_anterior, sort_keys=True)
        hash_recalculado = hashlib.sha256(json_anterior.encode()).hexdigest()
        
        link_intacto = bloco_atual["hash_anterior"] == bloco_anterior["hash_atual"]
        conteudo_integro = hash_recalculado == bloco_anterior["hash_atual"]
        
        if link_intacto and conteudo_integro:
            print(f" Bloco {i} dados íntegros e validados.")
        else:
            print(f" ERRO NO BLOCO {i}: O elo com o Bloco {i-1} foi QUEBRADO!")
            if not conteudo_integro:
                print(f" Motivo: O conteúdo do Bloco {i-1} foi modificado!")
            cadeia_valida = False
        
    if cadeia_valida:
        print(" RESULTADO: Blockchain 100% íntegra e confiável.\n")
    else:
        print(" RESULTADO: ALERTA! Cadeia corrompida! Histórico rejeitado.\n")


print("=" * 65)
print("   RASTREABILIDADE ALIMENTAR")
print("=" * 65)

hash_inicial = "0" * 64
bloco0 = registrar_etapa("LOTE-BOI-774", "Gado comum íntegro", hash_inicial)
bloco1 = registrar_etapa("LOTE-BOI-774", "Processado e embalado a -18°C", bloco0["hash_atual"])
bloco2 = registrar_etapa("LOTE-BOI-774", "Recebido no estoque, pronto para venda", bloco1["hash_atual"])

cadeia_alimentar = [bloco0, bloco1, bloco2]

print("\n --- HISTÓRICO ORIGINAL ---")
exibir_historico(cadeia_alimentar)
validar_cadeia(cadeia_alimentar)

print("-" * 65)
input(" Pressione ENTER para simular a fraude no primeiro bloco...")
print("-" * 65)

print("\n Alterando o status do Bloco 0 de 'Gado comum' para 'Carne Nobre Angus'...")
cadeia_alimentar[0]["dados"]["status"] = "Carne Nobre Angus"

print("\n --- HISTÓRICO APÓS A TENTATIVA DE FRAUDE ---")
exibir_historico(cadeia_alimentar)
validar_cadeia(cadeia_alimentar)
