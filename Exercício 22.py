valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
while valor2 == 0:
    valor2 = int(input("Número inválido, digite valor2 novamente:"))

divisao = valor1/valor2
print(divisao)