print('-' * 30)
print("ANO DE NASCIMNETO")
print('-'*30)

nomes = []
anos =[]

for i in range(1,3):
    pessoas = input("digite um nome: ")
    nomes.append(pessoas)
    idade = int(input("digite sua idade: "))
    anos.append(idade)
    
for d in range(len(nomes)):
    if anos[d] >= 18:
        maior = "sim"
    else:
        maior = "nao"
    
for f in range(len(nomes)):
    print("nome: ", nomes[f], "idade: ", anos[f], "e maior de idade?:",  maior )