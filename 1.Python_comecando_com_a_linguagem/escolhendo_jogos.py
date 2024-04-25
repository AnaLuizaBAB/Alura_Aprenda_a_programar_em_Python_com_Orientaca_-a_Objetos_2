import forca
import adivinhacao

def escolha_jogo():
    print("\n\n")
    print ("Seja bem vindo!!! Escolha o jogo que deseja jogar.")
    print("\n")

    print("(1) Adivinhação    (2) Forca")
    jogo = int(input("Informe qual dos jogos irá jogar: "))

    if ( jogo == 1):
        print("Você escolheu o jogo da Adivinhação.")
        adivinhacao.jogar()
    elif(jogo == 2):
        print ("Você escolheu o jogo da Forca.")
        forca.jogar()

if(__name__ == "__main__"):
    escolha_jogo()