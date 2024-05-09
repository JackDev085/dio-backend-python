from pydantic import BaseModel,field,PositiveFloat
from typing import Annotated
class Atleta(BaseModel):
  nome: Annotated[str, field(description="nome do atleta", examples="joao", max_length="50")]
  cpf: Annotated[str, field(description="cpf do atleta", examples="12345678901", max_length="11")]
  idade: Annotated[int, field(description="idade do atleta", examples="25")]
  peso: Annotated[PositiveFloat, field(description="peso do atleta", examples="50.6")]
  altura: Annotated[PositiveFloat, field(description="altura do atleta", examples="1.80")]
  sexo: Annotated[str, field(description="sexo do atleta", examples="M or F")]