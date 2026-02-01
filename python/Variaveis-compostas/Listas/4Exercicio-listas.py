def ini():
    print('=-' *30)
    
ini()
print("NUMEROS FACIL")
ini()

numbers = []
while True:
    usu = int(input("digite um numero: "))
    numbers.append(usu)
    cont = input("deseja continuar?(S/N): ").upper()
    if cont == "N":
       print("foram digitados", len(numbers), "numeros")
       numbers.sort(reverse=True)
       print(numbers)
       if 5 in numbers:
           print("o numero 5 faz parte da lista")
       else:
           print("o numero 5 nao faz oarte da lista")
       break
       
