import sys
import os
from datetime import datetime
from groq import Groq

# Configuração
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
diario_path = os.path.expanduser("~/diario_nexo.txt")
reg_dir = os.path.expanduser("~/expedicao/registros")
gps_path = os.path.expanduser("~/hardware_nexus.txt")

if not os.path.exists(reg_dir):
    os.makedirs(reg_dir)

def get_current_gps():
    if os.path.exists(gps_path):
        with open(gps_path, "r") as f:
            return f.read().strip()
    return "-27.5739, -48.6602"

def analisar_mensagem(prompt):
    gps_data = get_current_gps()
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": "Você é um Arqueólogo de Elite da Expedição NEXUS. Analise inscrições e achados com foco em arqueoastronomia, conexões transcontinentais e espiritualidade ancestral. Seja direto, técnico e inspire-se na jornada épica."}, {"role": "user", "content": f"Contexto GPS: {gps_data} | Passos Totais: $(python3 ~/expedicao/coletor_passos.py). Achado: {prompt}"}]
    )
    resultado = completion.choices[0].message.content
    
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    arquivo_log = f"{reg_dir}/registro_{ts}.txt"
    
    # Salvar registro com coordenadas gravadas no log
    with open(arquivo_log, "w") as f:
        f.write(f"--- REGISTRO ANCESTRAL [{ts}] ---\nGPS: {gps_data} | Passos Totais: $(python3 ~/expedicao/coletor_passos.py)\n\n{resultado}")
    
    with open(diario_path, "a") as f:
        f.write(f"\n👣 {datetime.now().strftime('%d/%m')} - Expedição em {gps_data}: {prompt[:40]}... (Log: {arquivo_log.split('/')[-1]})")
        
    return resultado

if len(sys.argv) > 1:
    print(analisar_mensagem(" ".join(sys.argv[1:])))
else:
    print("Erro: Descreva a inscrição.")
