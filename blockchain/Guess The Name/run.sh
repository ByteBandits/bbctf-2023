#!/bin/bash

IMAGE="$1"
PORT="$2"
HTTP_PORT=8545
SHARED_SECRET="7e8306aca5ab4eeeaac5c6b99715c8733b936f36d162513a552caac87b90"
FLAG="flag{A1l_17s_r3quirED_is_a_1iI7lE_5oliDity}"
ETH_RPC_URL="https://eth-goerli.g.alchemy.com/v2/bZbmrZezKTT7LL-T1WX-sJCPA6XFdgtN"

echo "[+] running challenge"
exec docker run \
    -e "PORT=$PORT" \
    -e "HTTP_PORT=$HTTP_PORT" \
    -e "ETH_RPC_URL=$ETH_RPC_URL" \
    -e "FLAG=$FLAG" \
    -e "PUBLIC_IP=$PUBLIC_IP" \
    -e "SHARED_SECRET=$SHARED_SECRET" \
    -p "$PORT:$PORT" \
    -p "$HTTP_PORT:$HTTP_PORT" \
    -d \
    "$IMAGE"
