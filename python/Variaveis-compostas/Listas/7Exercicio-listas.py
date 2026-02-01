def ini():
    print('-' *30)
ini()
print("PESSOAS E PESOS")
ini()

cad = []
dados = []
while True:
    cad.append(input("digite seu nome: "))
    cad.append(int(input("digite seu peso: ")))
    dados.append(cad[:])
    cad.clear()
    cont = input("deseja cobtinuar?(S/N): ").upper()
    if cont == 'N':
            print(f'pessoaa cadastradas: {len(dados)}')
            break
maior = dados[0][1]

for pessoa in dados:
    if pessoa[1] > maior:
        maior = pessoa[1]
        
print(f'maior peso: {maior}')

maiores = []
for pessoa in dados:
    if pessoa[1] >= 100 :
        maiores.append(pessoa)
print("maiores pesos:")
print(maiores)