matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0

# leitura da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)

        if valor % 2 == 0:
            soma_pares += valor

        if coluna == 2:
            soma_terceira_coluna += valor

# mostrar a matriz formatada
print('-=' * 20)
for linha in matriz:
    for valor in linha:
        print(f"[ {valor:^5} ]", end='')
    print()

# maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

print('-=' * 20)
print(f"A soma dos valores pares é: {soma_pares}")
print(f"A soma dos valores da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {maior_segunda_linha}")