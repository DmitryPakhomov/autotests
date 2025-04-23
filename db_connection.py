import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Настройки подключения к БД, берём из .env
DB_HOST = os.environ['HOST']
DB_PORT = int(os.environ['PORT'])
DB_USER = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DATABASE']
SSH_LOCAL_PORT = int(os.environ['SSH_LOCAL_PORT'])

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)  # Для основных логов
logging.getLogger('sqlalchemy.dialects').setLevel(logging.DEBUG)  # Для параметров запросов


def create_session(use_tunnel: bool = False, local_port: int = SSH_LOCAL_PORT):
    """Создаёт сессию SQLAlchemy, учитывая использование туннеля."""
    if use_tunnel:
        db_host_var = "127.0.0.1"
        db_port_var = local_port
    else:
        db_host_var = DB_HOST
        db_port_var = DB_PORT

    engine = create_engine(
        f"mariadb+mariadbconnector://{DB_USER}:{DB_PASSWORD}@{db_host_var}:{db_port_var}/{DB_NAME}",
        pool_pre_ping=True,
        pool_recycle=5,
        connect_args={"connect_timeout": 20, "read_timeout": 20, "write_timeout": 20}
    )
    return sessionmaker(bind=engine)
