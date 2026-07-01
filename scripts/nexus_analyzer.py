import json
import os

def analisar_desempenho():
    path = "/data/data/com.termux/files/home/expedicao/data/expedicao_data.json"
    if not os.path.exists(path):
        print("Erro: Nenhum dado de expedição encontrado.")
        return
        
    with open(path, "r") as f:
        logs = [json.loads(line) for line in f]
    
    print(f"\n--- ANALISE NEXUS V6 ---")
    print(f"Pontos mapeados: {len(logs)}")
    
    criticos = [p for p in logs if int(p['infra_index']) <= 2]
    print(f"Pontos de risco (Nota <= 2): {len(criticos)}")
    
    if len(logs) > 0:
        media = sum(int(p['infra_index']) for p in logs) / len(logs)
        print(f"Nota média da rota: {media:.2f}")
    print("------------------------\n")

if __name__ == "__main__":
    analisar_desempenho()
