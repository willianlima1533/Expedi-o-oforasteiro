import os
import subprocess
import google.generativeai as genai

# Configuração da API de Visão
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def analisar_foto(caminho_foto):
    foto = genai.upload_file(caminho_foto)
    response = model.generate_content(["Analise esta imagem arqueológica. Identifique inscrições, padrões geométricos, estado de conservação e possível origem cultural. Seja técnico.", foto])
    return response.text

# Captura
foto_path = "/sdcard/DCIM/expedicao_temp.jpg"
subprocess.run(["termux-camera-photo", foto_path])

# Análise
if os.path.exists(foto_path):
    print("Analisando imagem...")
    resultado = analisar_foto(foto_path)
    with open(os.path.expanduser("~/expedicao/log_visual.txt"), "w") as f:
        f.write(resultado)
    print(resultado)
