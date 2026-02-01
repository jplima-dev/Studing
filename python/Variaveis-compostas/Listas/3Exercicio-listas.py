def ini():
    print('=-'*23)
    
ini()
print("NUMEROS NO CANTO")
ini()

numbers = []

for i in range(5):
    usuario = int(input("digite um numero: "))

    if usuario not in numbers:
        if len(numbers) == 0:
            numbers.append(usuario)
        else:
            for pos in range(len(numbers)):
                if usuario < numbers[pos]:
                    numbers.insert(pos, usuario)
                    break
            else:
                numbers.append(usuario)

print(numbers)