def lin():
    print('-' *40)
    
lin()
print("TABUADA QUE PARA COM NUMERO NEGATIVO")
lin()

while True:
    usuario = int(input("digite um numero para ver sua tabuada: "))
    if usuario <= 0:
        print("numero invalido")
        print("Encerrando...")
        break
    for i in range(1, 11):
        print(f'{usuario} * {i}: ', usuario * i)
    lin()