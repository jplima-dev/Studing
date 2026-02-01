def ini():
    print('-' *30)
    
ini()
print("LISTA IMPARES E PARES")
ini()

numbers = [[], []]

for i in range(1,4):
    usu = int(input("Digite um numero: "))
    print("Numero adcionado na lista...")
   
    if usu % 2 == 0:
        numbers[0].append(usu)
    else:
        numbers[1].append(usu)
numbers[0].sort()
numbers[1].sort()
print(f'numeros pares: {numbers[0]}')
print(f'numeros impares: {numbers[1]}')