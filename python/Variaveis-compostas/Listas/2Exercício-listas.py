def ini():
    print('=-' *30)
    
ini()
print("NUMEROS ORDEM CRESCENTE")
ini()

numeros = []

while True:
    usuario = int(input("digite um numero: "))
    if usuario not in numeros:
        numeros.append(usuario)
    cont = input("deseja continuar?(s/n): ").upper()
    
    if cont == "N":
        numeros.sort()
        print(numeros)
        break
   