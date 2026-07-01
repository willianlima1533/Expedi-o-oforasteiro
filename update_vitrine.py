import os
import sys
import datetime

readme_path = "README.md"

def atualizar_vitrine(nome_arquivo):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    nova_linha = f"- **[{timestamp}] Nova Coleta de Campo:** {nome_arquivo} | [Solicitar acesso](https://tally.so/r/RGga1J)\n"
    
    if not os.path.exists(readme_path):
        print("README.md não encontrado!")
        return

    with open(readme_path, "r") as f:
        linhas = f.readlines()
        
    for i, linha in enumerate(linhas):
        if "### 📡 STATUS DA MISSÃO" in linha:
            linhas.insert(i + 2, nova_linha)
            break
            
    with open(readme_path, "w") as f:
        f.writelines(linhas)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        atualizar_vitrine(sys.argv[1])
        print(f"Vitrine atualizada com: {sys.argv[1]}")
