import os
import sys
from groq import Groq

# Configuração de segurança
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def pensar_nexus(pergunta):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Você é o NEXUS V6, o Co-Criador de Elite."},
                {"role": "user", "content": pergunta}
            ],
            temperature=0.6,
            max_tokens=1500
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Erro no Córtex Groq: {str(e)}"

if __name__ == "__main__":
    print("NEXUS Intelligence Online. Aguardando input...")
    # Loop simples para manter o processo ativo
    import time
    while True:
        time.sleep(60)
