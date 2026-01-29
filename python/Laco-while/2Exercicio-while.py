import random

ale = random.randint(1, 10)
tentativas = 0
usuario = ""
while ale != usuario:
    usuario = int(input("digite um numero: "))
    tentativas += 1
print("voçe fez em", tentativas, "tentativas")

