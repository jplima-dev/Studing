print('-' * 30)
print("PROGRESSÃO ARITMÉTICA")
print('-' * 30)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

contador = 1
termo = primeiro

while contador <= 10:
    print(termo, end=" ")
    termo += razao
    contador += 1