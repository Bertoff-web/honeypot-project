# 🍯 Honeypot Project

Honeypot que simula serviços SSH e HTTP falsos para detectar e registrar tentativas de acesso não autorizadas.

## Como funciona

Qualquer conexão nos serviços é automaticamente suspeita — usuários legítimos não sabem que eles existem. O sistema registra IP, horário e payload em JSON.

## Serviços simulados

| Serviço | Porta | O que captura |
|---------|-------|---------------|
| HTTP    | 8888  | Requisições, user-agent, payload |
| SSH     | 2222  | Banner, tentativas de login |

## Como rodar

```bash
python honeypot.py
```

## Exemplo de log gerado

```json
{"timestamp": "2026-05-18T12:12:01", "service": "HTTP", "attacker_ip": "127.0.0.1", "attacker_port": 62926, "payload": "GET / HTTP/1.1"}
```

## Tecnologias

- Python 3 (stdlib — sem dependências externas)
- Módulos: `socket`, `threading`, `logging`, `json`

