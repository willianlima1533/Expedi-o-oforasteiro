#!/bin/bash
echo "--- INICIANDO PROTOCOLO DE CHECK-IN ---"
~/sincronizar_gps.sh
# Verifica fadiga e notifica se necessário
STATUS_FADIGA=$(python3 ~/expedicao/monitor_fadiga.py)
if [[ $STATUS_FADIGA == *"ALERTA"* || $STATUS_FADIGA == *"AVISO"* ]]; then
    termux-notification --title "NEXUS: BIOMETRIA" --content "$STATUS_FADIGA" --id 998
fi
# Executa a análise
python3 ~/expedicao/analisador_ancestral.py "$*"
~/gta_notificar.sh
python3 ~/expedicao/monitor_fadiga.py
echo "--- REGISTRO FINALIZADO E SALVO ---"
