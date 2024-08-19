#media = 0
#soma = 0
#for i in range(10):
#   num = float(input("Informe o número: "))
#
#media = media + num
#total = media / 10
#
#   print(total)
soma = 0
contador = 0
for i in range(10):
    num = int(input("Digite a nota: "))
    if num >=0 and num <=10:
        soma = soma + num
        contador = contador + 1
        media = soma/contador
if contador != 0:
    media = soma/contador
    print(media)
else:
    print("Aprende a digitar")
