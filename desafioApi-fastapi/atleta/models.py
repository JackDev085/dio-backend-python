from sqlalchemy import Integer,String,Float, DateTime
from models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
class AtletaModel(BaseModel):
  __tablename__ = "atletas"
  pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
  nome: Mapped[str] = mapped_column(String(50), nullable=False)
  cpf: Mapped[str] = mapped_column(String(11), nullable=False)
  idade: Mapped[str] = mapped_column(Integer(11), nullable=False)
  peso: Mapped[Float] = mapped_column(Float(11), nullable=False)
  altura: Mapped[Float] = mapped_column(Float(11), nullable=False)
  sexo: Mapped[str] = mapped_column(String(1), nullable=False)
  created_as: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
  
  
  