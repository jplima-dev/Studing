print('-'*30)
print("PESOS DIFERENTES")
print('-'*30)

nomes = []
pesos = []

for i in range(1,6):
    usuario = input("digite o seu nome: ")
    nomes.append(usuario)
    massa = int(input("digite seu peso: "))
    pesos.append(massa)
    
maior = pesos[0]
menor = pesos[0]    
    
for peso in pesos:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
        
for a in range(len(nomes)):
    print("nome: ", nomes[a], "peso: ", pesos[a])
    
print("maior peso: ", maior)
print("menor peso: ", menor)
    
