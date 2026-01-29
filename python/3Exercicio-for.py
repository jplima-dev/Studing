print('-' *30)
print("MULTIPLOS DE 3")
print('-' *30)

soma = 0

for i in range(0,501):
    if  i % 2 != 0 and i % 3 == 0:
        soma += i
      
print(soma)