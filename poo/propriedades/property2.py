class Pessoa:
  def __init__(self,nome, idade) -> None:
    self.nome=nome
    self.idade = idade
    
  @property
  def x(self):
    return self.nome
  
  @x.setter
  def x(self,nome):
    self.nome = nome
    
  
a = Pessoa("Junio",12)
a.x="skadjaslk"
print(a.x)