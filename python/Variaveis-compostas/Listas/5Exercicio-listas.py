def ini():
    print('=-' *30)
    
ini()
print("3 LISTAS")
ini()

numbers = []
pares = []
impares = []
while True:
    usu = int(input("digite um numero: "))
    numbers.append(usu)
    print("numero sendo adcionado a lista...")
    
    cont = input("deseja continuar?(S/N): ").upper()
    if usu % 2 == 0:
        pares.append(usu)
    else:
        impares.append(usu)
    if cont == "N":
        print(f'numeros: {numbers}')
        print(f'numeros pares: {pares}')
        print(f'numeros impares: {impares}')
        break