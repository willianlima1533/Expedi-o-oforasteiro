#!/bin/bash
if ping -c 1 8.8.8.8 &> /dev/null; then
    exit 0
else
    termux-notification --title "NEXUS: Alerta de Rede" --content "Sem conexão. Dados em fila de espera." --priority high
    exit 1
fi
