def ini():
    print('-' *30)
    
ini()
print("NOTAS DE ALUNOS")
ini()

alunos = []

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    cont = input("Deseja continuar? (S/N): ").upper()
    if cont == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')

for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-=' * 30)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc < len(alunos):
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')