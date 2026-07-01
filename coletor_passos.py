import subprocess
import json

def get_steps():
    try:
        # Captura o contador de passos (step_count)
        result = subprocess.check_output(["termux-sensor", "-s", "step_count", "-n", "1"])
        data = json.loads(result.decode('utf-8'))
        # Retorna o valor do sensor
        return data.get("values", [0])[0]
    except:
        return 0

print(get_steps())
