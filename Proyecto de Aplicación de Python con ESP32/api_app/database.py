# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
 
 
# URL de connexió
DATABASE_URL = "sqlite:///sensors.db"
 
# Engine: la connexió al motor de BD
# echo=False  →  no mostra SQL per consola (True per depurar)
# check_same_thread=False  →  necessari per a SQLite amb FastAPI
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False}
)
 
# SessionLocal: factoria de sessions
# autocommit=False  →  cal fer db.commit() explícitament
# autoflush=False   →  no envia canvis fins al commit
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 
 
# Base: classe de la qual hereten tots els models
class Base(DeclarativeBase):
    pass
 
 
# Dependency per a FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
