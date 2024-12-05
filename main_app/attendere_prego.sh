#!/bin/bash
#Ricorda di fare: 
#   chmod +x ./attendere_prego.sh

HOST=$1
PORT=$2
TIMEOUT=${3:-60}

echo "Attendere prego, connessione a $HOST:$PORT in corso..."

for i in $(seq 1 $TIMEOUT); do
	nc -z $HOST $PORT
	if [ $? -eq 0 ]; then
		echo "Connessione a $HOST:$PORT effettuata!"
		exit 0
	fi
	echo "Tentativo numero $i: non ancora connessi a $HOST:$PORT, riprovando..."
	sleep 1
done

echo "Timeout raggiunto. $HOST:$PORT non disponibili."
exit 1

