resp = "s"
while resp == "s" or resp == "S":

    n = float(input("Digite um número: "))

    while n == 0:
        n = float(input("Digite um número válido: "))

    if n < 0:
        print("negativo")
    else:
        print("Positivo")

    resp = input("Deseja realizar novamente? [S/N]:")

    if resp == "n" or resp == "N":
        print("Você saiu")




