class Teste:
  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
  def __str__(self):
    return self.cor
class Teste2(Teste, ):
  def __init__(self, cor, modelo, ano, valor):
    super().__init__(cor, modelo, ano, valor)
  
  
b1 = Teste("azul", "monark", 2022,"R$2000")
b2 = Teste2("azul", "monark", 2022,"R$2000")
print(b2)