#!/bin/bash
# Pipeline de Elite: Resumo + Conversao de Ativos + Sync
echo "--- INICIANDO CONVERSAO DE ATIVOS DO FORASTEIRO ---"
python3 ~/expedicao/resumo_expedicao.py
python3 ~/expedicao/conversor_de_ativos.py
git add .
git commit -m "EXPEDICAO: Fechamento Automatizado 01/07/2026 13:02"
git push origin main
echo "--- ATIVOS SINCRONIZADOS E PRONTOS PARA MONETIZACAO ---"
