from abc import ABC
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
  @abstractmethod
  def ligar(self):
    pass
  
  @abstractmethod
  def desligar(self):
    pass

class ControleTv(ControleRemoto):
  def ligar():
    return "ligar tv"
  
  def desligar():
    return "desligar tv"

controle = ControleTv
print(controle.ligar())