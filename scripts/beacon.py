import subprocess
import json
import datetime
import os

def registrar_posicao():
    try:
        loc_raw = subprocess.check_output(['termux-location']).decode('utf-8')
        loc = json.loads(loc_raw)
        
        log_entry = {
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "lat": loc['latitude'],
            "lon": loc['longitude'],
            "alt": loc['altitude'],
            "status": "EM_MARCHA"
        }
        
        with open("/data/data/com.termux/files/home/expedicao/data/rastro.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        print(f"Rastro registrado: {log_entry['time']}")
    except Exception as e:
        print(f"Erro no rastro: {e}")

if __name__ == "__main__":
    registrar_posicao()
