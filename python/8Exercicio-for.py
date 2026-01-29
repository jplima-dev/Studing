print('-' * 30)
print("FRASE PALINDROMA")
print('-'*30)

frase = input("digite uma frase: ")
frase_coisada = frase.replace(" ", "").lower()
frase_ao_contrario = frase_coisada[:: -1]

if frase_coisada == frase_ao_contrario:
    print("essa frase e palindroma")
else:
    print("errou")