resp = "N"
resp2 = "S"
x = resp2

while x == resp2:
    idade = int(input("Digite a sua idade: "))
    anoatual = int(input("Digite o ano atual: "))
    mes = input("Já fez aniversário?[S/N]: ")

if mes == resp:
    anonasc = anoatual - (idade + 1)
    print("O ano que você nasceu é,", anonasc)
else:
    anonasc = anoatual - idade
    print("O ano que você nasceu é,", anonasc)

print(anonasc)

x = input("Você pretende fazer o calcúlo novamente?[s/n]: ")



