def lin():
    print('-' *30)
    
lin()
print("NUMEROS , PARA COM 999")
lin()

numeros = []
soma = 0

while True:
    usuario = int(input("digite um numero: "))
    if usuario == 999:
        break
        
    numeros.append(usuario)
    soma += usuario
    
    
        
print("seu numeros: ", soma)
print("quantidade de numeros: ", len(numeros))