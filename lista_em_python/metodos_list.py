numeros=[1,2,3,2,1,4,6,3,5,7,9,8,3,12]
#Count é utilizado como um contador, para verificar quantas vezez +
#dado um elemento repete em uma lista.
print(numeros.count(2)) #2
print(numeros.count(1)) #2


#Mesclagem de duas listas
lista1= ["a","b","c"]
lista2= ["d","e","f"]
lista1.extend(lista2)
print(lista1) #['a', 'b', 'c', 'd', 'e', 'f']

#Index:retorna a posição da primeira ocorrênca de um item na lista
numeros=[1,2,3,2,1,4,6,3,5,7,9,8,3,12]
print(numeros.index(4)) #5


#reverse: inverte uma lista
linguagens=["python", "c", "js", "java"]
linguagens.reverse() # ['java', 'js', 'c', 'python']
print(linguagens)

#Sort: Ordenação de listas
#Por ordem alfabética
linguagens=["python", "c","c#" "js", "java"]
linguagens.sort()  
print(linguagens) # ['c', 'c#js', 'java', 'python']

print("===================")

#Por ordem alfabética invertida
linguagens=["python", "c","c#" "js", "java"]
linguagens.sort(reverse=True) 
print(linguagens) # ['python', 'java', 'c#js', 'c']
print("===================")

#Pelo tamanho do elemento
linguagens=["python", "c","c#","js", "java"]
linguagens.sort(key=lambda x:(len(x))) 
print(linguagens) # ['c', 'c#', 'js', 'java', 'python']]
print("===================")

#Pelo tamanho do elemento e inverso
linguagens=["python", "c","c#","js", "java"]
linguagens.sort(key=lambda x:(len(x) ),reverse= True)
print(linguagens) # ['python', 'java', 'c#', 'js', 'c']
print("===================")

#Sorted: ordenacao de listas
linguagens=["python", "c","c#","js", "java"]
print(sorted(linguagens, key=lambda x:len(x))) # ['c', 'c#', 'js', 'java', 'python']

