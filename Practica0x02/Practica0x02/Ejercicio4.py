import socket as s
import sys
from concurrent.futures import ThreadPoolExecutor

# autor: Light221b


def scan_port(ip, port, protocol):
    try:
        sock_type = s.SOCK_STREAM if protocol == "TCP" else s.SOCK_DGRAM
        sock = s.socket(s.AF_INET, sock_type)
        sock.settimeout(0.1)  # Tiempo de espera de 0.5 segundos
        
        if protocol == "TCP":
            result = sock.connect_ex((ip, port))
            if result == 0:
                return port
        else: # UDP
            try:
                sock.sendto(b"", (ip, port))
                sock.recvfrom(1024)
                return port
            except s.timeout:
                return port # Si no se recibe respuesta, se considera que el puerto está abierto
            except Exception:
                pass
        sock.close()
    except Exception as e:
        print(f"Error al escanear el puerto {port}: {e}")
    return None


            

def scan_ports(ip, start_port, end_port, protocol):
    """
    Realiza el escaneo de los puertos en un rango y una dirección IP dada, utilizando el protocolo especificado (TCP o UDP).
    Retorna:
    list: Una lista de puertos abiertos en el rango dado y utilizando el protocolo especificado.
    """
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port, protocol) for port in range(start_port, end_port + 1)]
        open_ports = [future.result() for future in futures if future.result() is not None]
        
        for future in futures:
            port= future.result()
            if port:
                open_ports.append(port)
    return open_ports
    
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python3 scanner.py <IP> <Puerto Inicial> <Puerto Final> <TCP/UDP>")
        sys.exit()

    ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    protocol = sys.argv[4].upper()

    if protocol not in ["TCP", "UDP"]:
        print("Protocolo no válido. Debe ser TCP o UDP.")
        sys.exit()

    print(f"Escanenando puertos {protocol} del {start_port} al {end_port} en la dirección IP {ip}...")
    open_ports = scan_ports(ip, start_port, end_port, protocol)
    print("Puertos abiertos:", open_ports)

