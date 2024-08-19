outrapergunta = 0

while outrapergunta != 3:

    pergunta = int(input("DIGITE\n"
                         "1 PARA QUADRADO\n"
                         "2 PARA TRIÂNGULO\n"
                         "3 PARA SAIR:\n"))

    if pergunta == 1:
        lado = float(input("DIGITE O VALOR DO LADO DO QUADRADO: "))
        areaQ = lado ** 2
        print(areaQ)
    elif pergunta == 2:
        base = float(input("DIGITE O VALOR DA BASE DO TRIÂNGULO: "))
        altura = float(input("DIGITE O VALOR DA ALTURA DO TRIÂNGULO: "))
        areaT = (base * altura) / 2
        print(areaT)
    elif pergunta == 3:
        print("FIM DO PROGRAMA")
    else:
        print("Opção inválida")