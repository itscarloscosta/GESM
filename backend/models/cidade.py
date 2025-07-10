# backend/models/cidade.py
from sqlalchemy import Column, Integer, String
from database.database import Base

class Cidade(Base):
    __tablename__ = "cidades"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    estado = Column(String(2), nullable=False)
    logo_url = Column(String, nullable=True)