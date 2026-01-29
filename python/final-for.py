print('-' * 30)
print("DESAFIO FINAL")
print('-' * 30)

nomes = []
idades = []
sexos = []

for i in range(1, 5):  # exemplo com 4 pessoas
    nomes.append(input("Digite seu nome: "))
    idades.append(int(input("Digite sua idade: ")))
    sexos.append(input("Digite seu sexo (M/F): ").upper())

# média de idade
media = sum(idades) / len(idades)

# homem mais velho
maior_idade = 0
nome_mais_velho = ""

# mulheres com menos de 20
mulheres_menor_20 = 0

for i in range(len(nomes)):
    if sexos[i] == "M" and idades[i] > maior_idade:
        maior_idade = idades[i]
        nome_mais_velho = nomes[i]

    if sexos[i] == "F" and idades[i] < 20:
        mulheres_menor_20 += 1

print("-" * 30)
print("Média de idade:", media)
print("Homem mais velho:", nome_mais_velho, "-", maior_idade)
print("Mulheres com menos de 20 anos:", mulheres_menor_20)