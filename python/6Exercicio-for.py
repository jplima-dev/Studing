def lin():
    print('-' *30)
    
lin()
print("PROGRESSAO ARITIMETICA")
lin()

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

for i in range(10):
    termo = primeiro + i * razao
    print(termo)