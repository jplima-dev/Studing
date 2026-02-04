import random

def ini():
    print('-' * 30)

def dificuldade():
    print("ESCOLHA A DIFICULDADE")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 50)")
    print("3 - Difícil (1 a 100)")

    while True:
        try:
            op = int(input("Escolha a dificuldade: "))
            if op == 1:
                return 10
            elif op == 2:
                return 50
            elif op == 3:
                return 100
            else:
                print("Opção inválida, escolha 1, 2 ou 3.")
        except ValueError:
            print("Digite apenas números!")

def jogo(intervalo):
    comp = random.randint(1, intervalo)
    tentativas = 0
    pontos = 100
    jogos = 0
    while True:
        ini()
        print("TENTE ADIVINHAR O NÚMERO!!!")
        try:
            usu = int(input(f'Está entre 1 e {intervalo}: '))
        except ValueError:
            ini()
            print("Digite apenas números")
            continue

        tentativas += 1

        if usu < comp:
            ini()
            print("Errou, o número é maior!")
            pontos -= 5
        elif usu > comp:
            ini()
            print("Errou, o número é menor!")
            pontos -= 5
        else:
            ini()
            print("Parabéns!!!")
            print(f'Você fez {tentativas} tentativas!!!')
            print(f'Você ainda tem {pontos} pontos')
            tentativas = 0
            jogos += 1
            ini()
            cont = input("Deseja continuar? (S/N): ").upper()

            if cont == "S":
                ini()
                intervalo = dificuldade()
                comp = random.randint(1, intervalo)
            elif cont == 'N':
                try:
                    point = str(input("Digite seu nome para registro: "))
                except ValueError:
                    print("E pra colocar o nome animal")
                print("Retornando...")
                menu()


def menu():
    ini()
    print("JOGO DE ADIVINHAÇÃO")
    ini()
    print("1 - Iniciar jogo")
    print("2 - Placar de pontuação")
    print("3 - Sair")
    ini()

    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        return menu()

    if op == 1:
        ini()
        intervalo = dificuldade()
        jogo(intervalo)
    elif op == 3:
        print("Encerrando...")
        exit()

menu()
