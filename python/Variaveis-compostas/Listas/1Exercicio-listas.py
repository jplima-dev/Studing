def ini():
    print('=-' *30)
    
ini()
print("MAIOR E MENOR, POSICÇOES")
ini()

lista = []

for i in range(1,6):
    usuario = int(input("digite um valor: "))
    lista.append(usuario)
    
maior = lista[0]
menor = lista[0]

for num in range(len(lista)):
    if lista[num] > maior:
        maior = lista[num]
    if lista[num] < menor:
        menor = lista[num]
        
print(f'o maior numero e: {maior}')
print(f'o menor numero e: {menor}')
print("a posiçao do maior e: ", lista.index(maior) + 1)
print("a posiçao do menor e: ", lista.index(menor)+ 1)