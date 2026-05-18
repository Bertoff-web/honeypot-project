import socket
import threading
import config
from logger import log_event

def handle_ssh(conn, addr):
    ip, port = addr
    log_event("SSH", ip, port)
    try:
       
        conn.send(b"SSH-2.0-OpenSSH_8.9p1 Ubuntu\r\n")
        data = conn.recv(1024)
        log_event("SSH", ip, port, data.decode(errors="ignore"))
    except Exception:
        pass
    finally:
        conn.close()

def handle_http(conn, addr):
    ip, port = addr
    try:
        data = conn.recv(4096).decode(errors="ignore")
        log_event("HTTP", ip, port, data.split("\r\n")[0])  
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n\r\n"
            "<html><body><h1>Login</h1>"
            "<form><input name='user'/><input name='pass' type='password'/>"
            "<button>Entrar</button></form></body></html>"
        )
        conn.send(response.encode())
    except Exception:
        pass
    finally:
        conn.close()

def start_server(port, handler, service_name):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((config.HOST, port))
    server.listen(5)
    print(f"[*] {service_name} honeypot ouvindo na porta {port}")
    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handler, args=(conn, addr))
        t.daemon = True
        t.start()

if __name__ == "__main__":
    print("[*] Honeypot iniciado. Ctrl+C para parar.\n")
    threads = [
        threading.Thread(target=start_server, args=(config.SSH_PORT, handle_ssh, "SSH")),
        threading.Thread(target=start_server, args=(config.HTTP_PORT, handle_http, "HTTP")),
    ]
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()
