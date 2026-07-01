#!/bin/bash
# Pipeline de Elite com Termux:API

echo "--- PROCESSANDO ATIVOS ---"
python3 ~/expedicao/resumo_expedicao.py
python3 ~/expedicao/conversor_de_ativos.py

# Faz o commit e push
git add .
git commit -m "EXPEDICAO: Ciclo 01/07/2026 13:03"
git push origin main

# Notificação nativa via Termux:API
termux-notification --title "NEXUS: Ciclo Fechado" --content "Ativos processados e sincronizados com sucesso." --priority high

echo "--- ATIVOS SINCRONIZADOS ---"
