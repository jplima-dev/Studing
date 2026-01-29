print('-' * 30)
print("PROGRESSÃO ARITMÉTICA")
print('-' * 30)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = primeiro
total = 0
mais = 10

while mais != 0:
    total += mais
    while total > 0:
        print(termo, end=" ")
        termo += razao
        total -= 1
    print()
    mais = int(input("Quantos termos a mais? (0 para sair): "))

print("Programa encerrado.")