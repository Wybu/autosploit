#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

fonts=("standard" "slant" "shadow" "digital" "block" "small")
random_font=${fonts[$RANDOM % ${#fonts[@]}]}

echo -e "${GREEN}"
figlet -f "$random_font" "AUTOS"
echo -e "${NC}"



echo -e "${RED}------------------------------------------${NC}"
echo -e "${RED}            Automatic Sploiter  ${NC}"
echo -e "${RED}------------------------------------------${NC}"
