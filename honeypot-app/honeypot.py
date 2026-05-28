import socket
import json
import sys
from datetime import datetime

HOST = '0.0.0.0'
PORT = 6379

def log_incident(attacker_ip, attacker_port, data):
    incident = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event_type": "HONEYPOT_TRIGGERED",
        "severity": "CRITICAL",
        "mitre_attack_tactic": "Discovery / Lateral Movement",
        "attacker_ip": attacker_ip,
        "attacker_port": attacker_port,
        "payload_received": data.decode('utf-8', errors='ignore').strip(),
        "message": "Unauthorized access attempt to deceptive Redis Honeypot!"
    }
    print(json.dumps(incident), flush=True)

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[*] Deceptive Defense Honeypot listening on port {PORT}...", flush=True)
    except Exception as e:
        print(f"[-] Failed to bind to port {PORT}: {e}", file=sys.stderr)
        sys.exit(1)

    while True:
        client_sock, client_addr = server.accept()
        attacker_ip, attacker_port = client_addr
        try:
            data = client_sock.recv(1024)
            if data:
                log_incident(attacker_ip, attacker_port, data)
                client_sock.sendall(b"-ERR Authentication required.\r\n")
        except Exception as e:
            pass
        finally:
            client_sock.close()

if __name__ == "__main__":
    start_honeypot()
