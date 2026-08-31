# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
 
 
# URL de connexión
DATABASE_URL = "sqlite:///sensors.db"
 
# Engine: la conexión al motor de BD
# echo=False  →  no muestra SQL por consola (True para depurar)
# check_same_thread=False  →  necesario para SQLite con FastAPI
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False}
)
 
# SessionLocal: factoria de sessions
# autocommit=False  →  hace falta hacer db.commit() explicitamente
# autoflush=False   →  no envia cambios hasta el commit()
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 
 
# Base: clase de la cual heredamos todos los valores
class Base(DeclarativeBase):
    pass
 
 
# Dependencia para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
