comecou = float(input("DE QUE HORAS COMEÇOU O JOGO DE XADREX? "))
terminou = float(input("DE QUE HORAS TERMINOU O JOGO DE XADREX? "))

if terminou >= comecou:
    duracao = terminou - comecou
    print(duracao)
else:
    duracao = comecou - terminou
    print(duracao)