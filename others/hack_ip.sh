#!/bin/bash

# --- CONFIGURACIÓN DE COLORES ---
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Limpiar pantalla
clear

# --- 1. INTRODUCCIÓN DEDSEC ---
echo -e "${CYAN}"
figlet "DEDSEC"
echo -e "${NC}"
echo -e "${WHITE}>> INICIANDO PROTOCOLO DE RASTREO DE RED...${NC}"
sleep 1

# --- 2. BARRA DE PROGRESO FALSA ---
echo -ne "${GREEN}CARGANDO EXPLOITS: ${NC}[                    ] 0%"
for i in {1..20}; do
    sleep 0.1
    echo -ne "\r${GREEN}CARGANDO EXPLOITS: ${NC}["
    for j in $(seq 1 $i); do echo -ne "#"; done
    for k in $(seq $i 19); do echo -ne " "; done
    echo -ne "] $((i*5))%"
done
echo -e "\n${GREEN}>> ACCESO CONCEDIDO.${NC}"
sleep 0.5

# --- 3. EFECTO MATRIX (Hex Dump falso) ---
echo -e "${CYAN}>> DESENCRIPTANDO TRÁFICO DE RED...${NC}"
sleep 1
# Bucle que dura 3 segundos mostrando basura hexadecimal
end=$((SECONDS+3))
while [ $SECONDS -lt $end ]; do
    # Genera cadenas aleatorias hexadecimales
    echo -e "${GREEN}$(head -c 30 /dev/urandom | xxd -p | head -n 1)  $(head -c 20 /dev/urandom | xxd -p | head -n 1)${NC}"
    sleep 0.05
done

# --- 4. MENSAJES DE SYSTEMA ---
echo -e "${RED}[!] FIREWALL DETECTADO. Bypassing...${NC}"
sleep 0.8
echo -e "${GREEN}[+] Bypass exitoso.${NC}"
sleep 0.4
echo -e "${CYAN}[*] Escaneando interfaces locales...${NC}"
sleep 0.5
echo -e "${CYAN}[*] Resolviendo dirección del nodo maestro...${NC}"
sleep 1

# --- 5. OBTENER IP REAL ---
# Intenta obtener la IP. Funciona en la mayoría de distros Linux.
MY_IP=$(hostname -I | awk '{print $1}')

# Si falla hostname, intenta ip route
if [ -z "$MY_IP" ]; then
    MY_IP=$(ip route get 1.1.1.1 | awk '{print $7}')
fi

# --- 6. MOSTRAR LA IP EN GRANDE ---
clear
echo -e "${RED}"
echo "=================================================="
echo "      ⚠️  OBJETIVO LOCALIZADO  ⚠️"
echo "=================================================="
echo -e "${NC}"
echo -e "${CYAN}TU IP DE ACCESO ES:${NC}"
echo ""

# Intentamos usar FIGLET si está instalado para que se vea GIGANTE
if command -v figlet &> /dev/null; then
    echo -e "${GREEN}"
    figlet "$MY_IP"
    echo -e "${NC}"
else
    # Si no tiene figlet, usamos un cuadro de texto grande
    echo -e "${GREEN}"
    echo "########################################"
    echo ""
    echo "       $MY_IP"
    echo ""
    echo "########################################"
    echo -e "${NC}"
fi

echo ""
echo -e "${WHITE}>> INTRODUCE ESTA IP EN EL TERMINAL DE MANDO${NC}"
echo -e "${WHITE}>> PULSA ENTER PARA CERRAR LA CONEXIÓN...${NC}"
read
clear
