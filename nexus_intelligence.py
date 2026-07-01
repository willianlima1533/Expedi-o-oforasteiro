# (Delete a linha que contém os caracteres "AIzaSy..." e salve com Ctrl+O, Enter, Ctrl+X)

# 2. Corrija o último commit que continha o segredo
git add nexus_intelligence.py
git commit --amend -m "Centralização do núcleo de inteligência (Removido segredo)"
import os
import sys
from groq import Groq

# API Key provisionada via Gatilho Seguro
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def pensar_nexus(pergunta):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Você é o NEXUS V6, o Co-Criador de Elite do usuário. Responda com termos técnicos de engenharia, logística avançada e estratégia. Seja direto, brilhante e aja como um braço direito operacional."},
                {"role": "user", "content": pergunta}
            ],
            temperature=0.6,
            max_tokens=1500
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Erro no Córtex Groq: {str(e)}"

if __name__ == "__main__":
    # Suporte para entrada via pipe (CLI) ou argumento
    if not sys.stdin.isatty():
        entrada = sys.stdin.read()
    else:
        entrada = " ".join(sys.argv[1:])
    
    if entrada.strip():
        print(pensar_nexus(entrada))
