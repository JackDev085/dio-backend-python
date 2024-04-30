numeros = [1,2,3,4,5,6,7,8,9,10,123,12,34,56,456]
        #Retorno - For -        Condicao
pares = [num for num in numeros if num%2==0]
print(pares) # [2, 4, 6, 8, 10, 12, 34, 56, 456]

numerosVezesDois =[num*2 for num in numeros]
print(numerosVezesDois) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 246, 24, 68, 112, 912]