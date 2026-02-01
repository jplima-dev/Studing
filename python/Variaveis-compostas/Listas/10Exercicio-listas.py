import random

def ini():
    print('-' *30)
    
ini()
print("PALPITES MEGA SENA")
ini()

pal = int(input("quantos palpites vc quer?: "))
numeros = int(input("digite de a quantidade de numeros: "))

lista = []

for i in range(pal):
    palpite = []
    while len(palpite) < numeros:
        num = random.randint(1, 60)
        if num not in palpite:
            palpite.append(num)
    lista.append(palpite)
            
print(f'palpites: {lista}')
    