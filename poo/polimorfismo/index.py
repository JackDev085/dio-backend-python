#Polimorfismo é utilizado para mudar o contexto de uma função
#para diferentes tipo de utilização

class Animal:
  def __init__(self,nome) -> None:
    self.nome=nome
  def andar(self):
    return f"{self.nome} está andando"
class Cobra(Animal):
  def __init__(self, nome) -> None:
    super().__init__(nome)
  def andar(self):
    return f"{self.nome} está rastejando"  
  
rato =Animal("rato")
cobra = Cobra("cobra")
print(cobra.andar())

print(rato.andar())