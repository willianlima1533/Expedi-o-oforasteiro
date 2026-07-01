import subprocess
import json

def check_fadiga():
    try:
        result = subprocess.check_output(["termux-sensor", "-s", "step_count", "-n", "1"])
        data = json.loads(result.decode('utf-8'))
        passos = int(data.get("values", [0])[0])
        
        if passos > 15000:
            subprocess.run(["termux-notification", "--title", "NEXUS: ALERTA TÁTICO", "--content", "Fadiga detectada. Recomendada pausa estratégica para reidratação.", "--id", "100"])
            return "ALERTA: FADIGA ALTA"
        return "Status: Operacional"
    except:
        return "Status: Sensores offline"
