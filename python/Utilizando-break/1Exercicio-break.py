def lin():
    print('-' *20)
    
lin()
print("PARAR COM 999")
lin()

numeros = []
total = 0

while True:
    n = int(input("digite um numero: "))
    if n == 999:
        print("Encerrando...")
        break
    numeros.append(n)
    total += n

quantidade = len(numeros)

print("total digitado: ", quantidade)
print("todos 0os numeros somados: ", total)
