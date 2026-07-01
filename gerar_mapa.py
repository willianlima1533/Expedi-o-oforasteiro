import os
import glob
import re

reg_dir = os.path.expanduser("~/expedicao/registros")
kml_file = os.path.expanduser("~/expedicao/mapa_expedicao.kml")
registros = glob.glob(f"{reg_dir}/registro_*.txt")

def extract_gps(text):
    match = re.search(r"GPS: ([\d.-]+), ([\d.-]+)", text)
    if match:
        return f"{match.group(2)},{match.group(1)}" # KML é Lon,Lat
    return "-48.6602,-27.5739" # Padrão se falhar

kml_content = '<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Expedicao Nexus</name>'

for r in registros:
    with open(r, "r") as log:
        content = log.read()
        coord = extract_gps(content)
        kml_content += f'''
    <Placemark>
      <name>{os.path.basename(r)}</name>
      <Point><coordinates>{coord},0</coordinates></Point>
    </Placemark>'''

kml_content += '</Document></kml>'
with open(kml_file, "w") as f:
    f.write(kml_content)
print(f"Mapa atualizado em: {kml_file}")
