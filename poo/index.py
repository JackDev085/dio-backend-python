class Bicicleta:
  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
    self.vendas=0
    self.venda()
    
  def buzina(self):
    return f"está buzinando! Beeeeeeee"
  def correr(self): 
    return f"está correndo! vrummmmmm"
  def parar(self):
    return f"está parando! treeeeeeee"
  def venda(self):
    self.vendas+=1
    return f"Número de vendas {self.vendas}"
  # def __str__(self):
  #   return f"{self.cor, self.modelo, self.ano,self.valor}"
  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

carol = Bicicleta("azul", "monark", 2022,"R$2000")
print(carol)

