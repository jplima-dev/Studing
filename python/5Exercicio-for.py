def lin():
    print('-' *30)
    
lin()
print("SEIS NUMEROS PAR")
lin()

soma = 0
pares = []

for n in range(1,7):
    usuario = int(input("digite um numero inteiro: "))
    
    if usuario % 2 == 0:
        pares.append(usuario)
        soma += usuario
        
print(pares)
print(soma)