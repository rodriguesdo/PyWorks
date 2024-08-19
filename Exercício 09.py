tipo = input("Digite g para gasolina \n e para etanol: ")
qtdLitros = float(input("Quantos litros você quer abastecer?: "))

lg=5.8
le=4.9

if tipo == 'g' or tipo == 'G':
    total = lg*qtdLitros
    print(f"Você gastou {total}")
elif tipo == 'e' or tipo == 'E':
    total = le*qtdLitros
    print(f"Você gastou {total}")
else:
    print("Errou")