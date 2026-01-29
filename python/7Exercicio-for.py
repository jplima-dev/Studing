def lin():
    print('-' *30)
    
lin()
print("NUMERO PRIMO")
lin()

usuario = int(input("digite um numero: "))

if usuario <= 1:
    print(usuario, "nao e primo")
else:
    primo = True
    for i in range(2, usuario):
            if usuario % i == 0:
                primo = False
                break
                
if primo:
    print(usuario, "e primo")
else:
    print(usuario, "nao e primo")