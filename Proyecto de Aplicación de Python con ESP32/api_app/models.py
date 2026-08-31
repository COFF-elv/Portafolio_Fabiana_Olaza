# models.py
from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base   # Base definida a database.py
 
 
class Lectura(Base):
    """
    Representa la taula "lectures" a SQLite.
    Cada instancia d'aquesta classe és una fila de la taula.
    """
    __tablename__ = "lectures"
 
    # Mapped[tipus] = type hint Python
    # mapped_column() = opcions de la columna SQL
    id:         Mapped[int]   = mapped_column(Integer, primary_key=True)
    sensor:     Mapped[str]   = mapped_column(String,  nullable=False)
    valor:      Mapped[float] = mapped_column(Float,   nullable=False)
    unitat:     Mapped[str]   = mapped_column(String,  nullable=False)
    dispositiu: Mapped[str]   = mapped_column(String,  nullable=False)
    timestamp:  Mapped[str]   = mapped_column(String,  nullable=False)


class Parameters(Base):
    """
    Representa la taula "Parameters" a SQLite.
    Cada instancia d'aquesta classe és una fila de la taula.
    """
    __tablename__ = "Parameters"
 
    # Mapped[tipus] = type hint Python
    # mapped_column() = opcions de la columna SQL
    id:         Mapped[int]   = mapped_column(Integer, primary_key=True)
    likes_limit:     Mapped[int]   = mapped_column(Integer,  nullable=False)
    aforo:      Mapped[int] = mapped_column(Integer,   nullable=False)
    timestamp:  Mapped[str]   = mapped_column(String,  nullable=False)