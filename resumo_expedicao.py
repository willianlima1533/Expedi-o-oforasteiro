import os
import glob
from datetime import datetime

# Localização do sensor (leitura do arquivo hardware_nexus.txt ou GPS atual)
def get_gps():
    try:
        with open(os.path.expanduser("~/hardware_nexus.txt"), "r") as f:
            return f.read().strip()
    except:
        return "-27.5739, -48.6602"

reg_dir = os.path.expanduser("~/expedicao/registros")
registros = glob.glob(f"{reg_dir}/registro_*.txt")

print("\n" + "="*40)
print("   📊 MAPA TÁTICO DE EXPEDIÇÃO")
print("="*40)
print(f"Coordenada Atual: {get_gps()}")
print(f"Descobertas Catalogadas: {len(registros)}")

if registros:
    print(f"Última posição registrada: {datetime.fromtimestamp(os.path.getmtime(registros[-1])).strftime('%d/%m/%Y')}")
    print("\nLogs recentes:")
    for r in registros[-3:]:
        print(f"-> {os.path.basename(r)}")
else:
    print("Nenhum dado de geolocalização coletado ainda.")

print("="*40 + "\n")
