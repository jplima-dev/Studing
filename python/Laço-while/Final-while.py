def lin():
    print('-' *30)
    
lin()
print("MEDIA DE NUMEROS")
lin()

numeros = []
soma = 0

while True:
    usuario = int(input("digite um numero: "))    
    numeros. append(usuario)
    soma += usuario
    
    usu = input("deseja continuar?(s/n): ").lower()
    if usu != "s":
        print("Encerrando...")
        break
        
maior = numeros[0]
menor = numeros[0]
    
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
        
quantidade = len(numeros)
media =  soma / quantidade

print("quantos numeros vc digitou: ", quantidade)
print("a media dos seu numeros: ", media)
print(maior)
print(menor)
    
    
    
    
    
    

    