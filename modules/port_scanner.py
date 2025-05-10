import socket

def scan_ports(ip, ports=[80, 443, 22, 21, 25]):
    open_ports = []
    for port in ports:
        sock = socket.socket()
        sock.settimeout(1)
        try:
            sock.connect((ip, port))
            open_ports.append(port)
        except:
            continue
        finally:
            sock.close()
    return open_ports
