#!/usr/bin/bash


RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # 

# ───────────── Banner ─────────────
clear
echo -e "${GREEN}${BOLD}"
echo "───────────────────────────────────────────────"
echo "🛡️   Net_Scan - Port & Subdomain Scanner       "
echo "───────────────────────────────────────────────"
echo -e "${NC}${CYAN}Author : Knightc0de"
echo -e "GitHub : https://github.com/Knightc0de"
echo -e "Tool   : Fast Recon Scanner${NC}"
echo


# ─────────────── Menu ───────────────
echo -e "${CYAN}Choose an option to run:${NC}"
echo "1) Port Scanner"
echo "2) Subdomain Scanner"
echo "3)  Mac Address Detection"
echo "4) Exit"
read -p "➤ Enter your option [1/2/3/4]: " opt

case "$opt" in
  1)
    echo -e "${YELLOW}\n[~] Launching Port Scanner...${NC}"
    read -p "Target IPv4: " ip
    read -p "Protocol TCP, UDP or both : " proto
    read -p "Start Port (default=1): " start
    read -p "End Port (default=1000): " end
    read -p "Threads (default=500): " threads
    read -p "Verbose? [y/N]: " verbose
    if [[ "$verbose" == "y" || "$verbose" == "Y" ]]; then
      python3 ./scripts/port_scanner.py --host "$ip" --proto proto -s "${start:-1}" -e "${end:-1000}" -t "${threads:-500}" -v
    else
      python3 ./scripts/port_scanner.py --host "$ip" --proto proto  -s "${start:-1}" -e "${end:-1000}" -t "${threads:-500}"
    fi
    ;;
  2)
    echo -e "${YELLOW}\n[~] Launching Subdomain Scanner...${NC}"
    read -p "Target Domain (e.g., example.com): " domain
    read -p "Wordlist file (default=wordlist.txt): " wordlist
    read -p "Threads (default=500): " threads
    read -p "Verbose? [y/N]: " verbose
    if [[ "$verbose" == "y" || "$verbose" == "Y" ]]; then
      python3 ./scripts/sub_scanner.py "$domain" -w "${wordlist:-wordlist.txt}" -t "${threads:-500}" -v
    else
      python3 ./scripts/sub_scanner.py "$domain" -w "${wordlist:-wordlist.txt}" -t "${threads:-500}"
    fi
    ;;
  
  3) 
      echo -e "${YELLOW}\n[~] Launching MAC Detection Scanner...${NC}"
      read -p "Target IP Range (e.g., 192.168.1.0/24): " net_range
      python3 ./scripts/mac_detect.py "$net_range"
    ;;

  4)
    echo -e "${RED} Exiting... ${NC}"
    exit 0
    ;;
  *)
    echo -e "${RED}[!] Invalid option. Please try again.${NC}"
    exit 1
    ;;
esac

