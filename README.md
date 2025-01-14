# seguridad-ofensiva-practicas
Practicas realizadas en el seminario de seguridad ofensiva. Algunas de ellas fueron realizadas en colaboracion. 



## Práctica 0x02

### Ejercicio 1
Este ejercicio realiza un ataque de fuerza bruta utilizando un diccionario de contraseñas para intentar acceder a un servidor SSH. El script `script.sh` toma como argumentos la IP, el puerto, el nombre de usuario y la ruta del diccionario de contraseñas, e intenta autenticarse con cada contraseña del diccionario hasta encontrar una válida.

### Ejercicio 3
Este ejercicio realiza un escaneo de red para identificar dispositivos activos y determinar su sistema operativo probable. El script `Ejercicio3.ps1` utiliza el comando `Test-Connection` para hacer ping a un rango de direcciones IP y, basado en el TTL (Time To Live) de la respuesta, infiere si el dispositivo está ejecutando Linux/Unix, Windows o un sistema operativo desconocido.

### Ejercicio 4
Este ejercicio realiza un escaneo de puertos en una dirección IP dada utilizando los protocolos TCP o UDP. El script `Ejercicio4.py` toma como argumentos la IP, el puerto inicial, el puerto final y el protocolo (TCP/UDP), y utiliza múltiples hilos para escanear los puertos en el rango especificado, identificando cuáles están abiertos.