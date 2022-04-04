import random
import os



def jogar():
    print('######################')
    print("### JOGO DA FORCA ####")
    print("######################")

    arquivo = open("palavras.txt", "r" )
    palavras=[]

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    
    palavra_secreta = palavras[numero].upper()

    letras_encontradas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_encontradas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_encontradas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_encontradas
        print(letras_encontradas)
    if(acertou):
        print("Voce Ganhou!!")
    else:
        print("voce Perdeu!!")
        print("Fim de Jogo!!")

jogar()
