def lin():
    print('-' *30)
    
lin()
print("TABUADA USANDO 'FOR'")
lin()

usuario = int(input("digite um numero: "))

for n in range(1,11):
    print(usuario, "* ", n,  "e: ", usuario * n)