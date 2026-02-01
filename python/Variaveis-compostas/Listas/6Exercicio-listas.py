def ini():
    print('-' *30)
    
ini()
print("EXPRESSOES")
ini()

usu = str(input("digite uma expressao matematica: "))
pilha = []

for pare in usu:
    if pare == '(':
        pilha.append('(')
    elif pare == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("sua expressao e valida")
else:
    print("sua expressao e invalida")
    