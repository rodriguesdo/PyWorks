n1 = float(input("Digite o primeiro valor:"))
while n1 < 0 or n1 > 10:
    n1 = int(input("Número inválido, digite novamnete um valor: "))

n2 = float(input("Digite o segundo valor: "))
while n2 < 0 or n2 > 10:
    n2 = float(input("Número inválido, digite novamente um valor:"))

media = (n1 + n2)/2
print(media)