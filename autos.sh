#!/bin/bash

PYTHON_BIN="/usr/bin/python3"
SCRIPT_PATH="e:/RepoGithub/autosploit/main.py"

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

CHECK_STEP=1


fonts=("standard" "slant" "shadow" "digital" "block" "small")
random_font=${fonts[$RANDOM % ${#fonts[@]}]}



echo -e "${GREEN}"
figlet -f "$random_font" "AUTOS"
echo -e "${NC}"


echo -e "${RED}------------------------------------------${NC}"
echo -e "${RED}            Automatic Sploiter  ${NC}"
echo -e "${RED}------------------------------------------${NC}"
while true; do
    if [ $# -lt 1 && CHECK_STEP==1]; then
    echo "Usage: $0 <target> [-s start_port] [-e end_port] [-S]"
    CHECK_STEP=0
    fi
    $PYTHON_BIN "$SCRIPT_PATH" "$@"

    if [[ "$input" == "quit" ]]; then
        break
    fi
    echo "Bye!"
done

