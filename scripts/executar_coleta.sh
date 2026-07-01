#!/bin/bash
echo "Iniciando coleta de dados de infraestrutura..."
python3 ~/expedicao/scripts/coleta_campo.py
echo "Sincronizando com o servidor..."
cd ~/expedicao
git add data/expedicao_data.json scripts/coleta_campo.py
git commit -m "Auto-sync: $(date)"
git push origin main
echo "Sucesso: Dados e scripts em nuvem."
