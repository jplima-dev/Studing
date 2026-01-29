import random

def lin():
    print('-' *30)
    
def linha_foda():
    print('-=' *15)
    
lin()
print("JOGO DE PAR OU IMPAR")
lin()

vitorias = 0

while True:
    impar_ou_par = input("digite impar ou par(i/p): ").lower()
    usuario = int(input("digite um numero: "))
    computador = random.randint(1, 10)

    # escolhas
    lin()
    print(f'vc escolheu {usuario}')
    print(f'o computador escolheu {computador}')
    lin()

    #calculos
    soma = usuario + computador
    print(f'a soma dos numeros deu {soma}') 
    lin()
    
    #verificaçao de impar ou par
    if soma % 2 == 0:
        soma = 'p'
    else:
         soma ='i'
     
     #resposta final
    if soma ==  impar_ou_par:
         print("Parabens vc ganhou!!!!!!!!")
         print("VAMOS DENOVO!!")
         vitorias += 1
         linha_foda()
    else:
          print("Vc perdeu que pena")
          print(f'voce venceu {vitorias} vezes')
          break
         

