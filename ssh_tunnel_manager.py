# ssh_tunnel_manager.py

from sshtunnel import SSHTunnelForwarder
import os
from dotenv import load_dotenv

load_dotenv()

# SSH-параметры берём из .ENV
SSH_HOST = os.environ['SSH_HOST']
SSH_PORT = int(os.environ['SSH_PORT'])
SSH_USER = os.environ['SSH_USER']
SSH_KEY_PATH = os.environ['SSH_KEY_PATH']
SSH_PASSPHRASE = os.environ['SSH_PASSPHRASE']
DB_HOST = os.environ['HOST']
DB_PORT = int(os.environ['PORT'])
SSH_LOCAL_PORT = int(os.environ['SSH_LOCAL_PORT'])

# Глобальный объект туннеля
tunnel = SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_pkey=SSH_KEY_PATH,
    ssh_private_key_password=SSH_PASSPHRASE,
    remote_bind_address=(DB_HOST, DB_PORT),
    local_bind_address=('127.0.0.1', SSH_LOCAL_PORT),
    set_keepalive=30.0
)


def start_tunnel():
    """Запуск SSH-туннеля"""
    if not tunnel.is_active:
        tunnel.start()
        print('Tunnel start')


def stop_tunnel():
    """Остановка SSH-туннеля"""
    if tunnel.is_active:
        tunnel.stop()
        print('Tunnel stop')
