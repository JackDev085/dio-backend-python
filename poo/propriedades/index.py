class Foo:
  def __init__(self,x) -> None:
    self._x = x
    
  @property
  def x(self):
    return self._x
  
  @x.setter
  def x(self,valor):
    self._x+=valor
  
  
  
a = Foo(10)
a.x=30
print(a.x)