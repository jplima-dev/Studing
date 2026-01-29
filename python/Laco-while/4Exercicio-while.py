print('-' * 30)
print("NUMERO FATORIAL")
print('-' * 30)

usuario = int(input("Digite um número: "))

fatorial = 1
contador = 1

while contador <= usuario:
    fatorial *= contador
    contador += 1

print("Fatorial de", usuario, "é", fatorial)