#!/usr/bin/env bash
if [[ -f "${STATIC_IP}" ]]; then
        echo "Using default IP from Docker"
else
        echo "Found static IP: ${STATIC_IP} using it"
        ifconfig eth0 ${STATIC_IP} netmask 255.255.255.0 up
fi
# sleep infinity
# python3 experimenter.py
# python3 peer_handler.py
# python3 main.py
