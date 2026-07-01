import subprocess
import json
import datetime
import os

def capturar_ponto():
    try:
        loc_raw = subprocess.check_output(['termux-location']).decode('utf-8')
        loc = json.loads(loc_raw)
    except:
        loc = {"latitude": 0, "longitude": 0}
    
    infra = input("Qual a qualidade da via (1-5)? ")
    
    data_ponto = {
        "timestamp": datetime.datetime.now().isoformat(),
        "latitude": loc.get("latitude"),
        "longitude": loc.get("longitude"),
        "infra_index": infra,
        "device_id": "nexus_expedicao_01"
    }
    
    path = os.path.expanduser("~/expedicao/data/expedicao_data.json")
    with open(path, "a") as f:
        f.write(json.dumps(data_ponto) + "\n")
    print(f"Log registrado em {path}")

if __name__ == "__main__":
    capturar_ponto()
