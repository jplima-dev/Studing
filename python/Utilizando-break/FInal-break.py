valor = int(input("Digite o valor a sacar: "))

cedula = 50
total_cedulas = 0

while True:
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"{total_cedulas} cédulas de R$ {cedula}")
        
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        
        total_cedulas = 0
        
        if valor == 0:
            break