#!/bin/bash
# Captura + Analise Imediata
DEST="~/expedicao/registros/foto_$(date +'%Y%m%d_%H%M%S').jpg"
termux-camera-photo -c 0 $(eval echo $DEST)
python3 ~/expedicao/analisador_visual.py
echo "--- REGISTRO E ANALISE FINALIZADOS ---"
