n = int(input("Digite um número: "))
resultado = 0
for k in range(1, 11):
    resultado = n*k
    print(k, "X", n, "=", resultado)