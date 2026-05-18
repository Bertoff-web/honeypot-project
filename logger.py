import logging
import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "honeypot.log")

os.makedirs(LOG_DIR, exist_ok=True)  
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(message)s"
)

def log_event(service, ip, port, data=None):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "service": service,
        "attacker_ip": ip,
        "attacker_port": port,
        "payload": data or ""
    }
    logging.info(json.dumps(event))
    print(f"[!] {service} — conexão de {ip}:{port}")