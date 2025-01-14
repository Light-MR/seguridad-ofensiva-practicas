# autor Light221b
# Importa el módulo necesario para Test-Connection
Import-Module Microsoft.PowerShell.Management

# Define el rango de direcciones IP a escanear para la interfaz Wi-Fi
$ipRange = 1..254 | ForEach-Object { "192.168.3.$_" } #modifique con su propia dirección IP

# Realiza el Network Sweep e intenta identificar el sistema operativo
$ipRange | ForEach-Object {
    try {
        $pingResult = Test-Connection -ComputerName $_ -Count 1 -ErrorAction Stop
        if ($pingResult) {
            $ttl = $pingResult.ResponseTimeToLive
            $os = if ($ttl -le 64) { "Linux/Unix" } elseif ($ttl -gt 64 -and $ttl -le 128) { "Windows" } else { "Desconocido" }
            "$($_) ACTIVO, Sistema Operativo probable: $os, TTL: $ttl"
        }
    } catch {
        "$($_) no alcanzable"
    }
}