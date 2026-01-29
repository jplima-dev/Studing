def lin():
    print('-' *30)

lin()
print("PRODUTOS E PREÇOS")
lin()

# variaveis globais

pro = []
pre = []
total = 0
mais_mil = 0
barato = None
nome_barato =""

# progrma principal

while True:
    usuario1 = input("Digite um produto para cadastro: ")
    usuario2 =  float(input("Digite o preço do produto: "))
    total += usuario2
    
    pro.append(usuario1)
    pre.append(usuario2)
    
    if usuario2 >= 1000:
        mais_mil += 1
    
    if barato is None or usuario2 < barato:
        barato = usuario2
        nome_barato = usuario1
        
    continuar = input("deseja continuar?(S/N): ").upper()
    if continuar == 'N':
        lin()
        print(f'total da compra: {total}')
        print(f'podutos acima de R$ 1000 reais: {mais_mil}')
        print(f'o produto mais barato e: {nome_barato} custando: R${barato}')
        break