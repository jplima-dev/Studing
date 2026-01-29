def l():
    print('-' *30)
    
l()
print("MENU DE CALCULADORA")
l()

n1 = int(input("digite um numero: ")) 
n2 = int(input("digite outro numero: "))

l()
while True:
    print("OQUE DESEJA FAZER?")
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos numeros")
    print("[5] encerrar")
    
    usuario = int(input(": "))
    
    # soma
    if usuario == 1:
        soma = n1 + n2
        print("a soma dos seus numeros e: ", soma)
        
        l()
        
    # multiplicaçao
    elif usuario == 2:
        mult = n1 * n2
        print("a multipliacaçao e: ", mult)
            
        l()
        
   # numero maior         
    elif usuario == 3:
        if n1 > n2:
            print(n1,"e maior que", n2)
        else:
            print(n1, "e menor que", n2)
            
        l()
    
    # novos numeros
    if usuario == 4:
        l()
        n1 = int(input("digite um novo numero: "))
        n2 = int(input(" digite outro novo numero: "))
    
    
    
    
    
    
    
    
    
    
    
    
    
    if usuario == 5:
        l()
        print("Encerrando...")
        break