idade = int(input("DIGITE A SUA IDADE: "))
meses = int(input("DIGITE O MÊS EM QUE VOCê NASCEU: "))
dias = int(input("QUANTOS DIAS FALTAM PARA VOCÊ COMPLETAR ANO: "))

anodias = idade*365
mesdias = meses*30

total = anodias + mesdias + dias

print(total)