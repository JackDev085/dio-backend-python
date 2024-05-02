#Encapsulamento é importante para delimitar controle de acesso a certas variáveis e escopos
#Variável privada = _var
#Variável pública = var

#Apesar do python não garantir que as varíaveis privadas sejam acessadas fora do escopo.
#Por convenção, é sabido que não se pode acessar diretamente essas variáveis.
class Conta:
  def __init__(self, saldo):
    self._saldo=saldo
    
    
  def deposita(self,valor):
    self._saldo += valor
    self.extrato()
    
  def extrato(self):
    print("Seu saldo é ", self._saldo)
    
    
c1 = Conta(200)
c1.deposita(100)