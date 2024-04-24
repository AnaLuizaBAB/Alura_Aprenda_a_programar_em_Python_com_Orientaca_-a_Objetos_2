import random

def jogar():

    print("\n\n")
    print ("Bem vindo ao jogo.")
    print("\n")

    numero_secreto = random.randrange(1,101)
    rodada = 1
    pontos = 1000

    print ("Informe o nível de dificuldade que deseja.")
    print("(1) Fácil    (2) Médio    (3) Difícil")

    nivel_de_dificuldade = int(input("\nQual nível de dificuldade que deseja: "))

    if(nivel_de_dificuldade == 1):
        numero_de_tentativas = 20
    elif(nivel_de_dificuldade ==2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5

    while(rodada <= numero_de_tentativas):

        print(f"\n***Tentativa número {rodada} de {numero_de_tentativas}***")
        chute = int(input ("Por favor informe o número de 1 a 100: "))
        print(f"\nVocê digitou o número {chute}. \n")

        if ( chute < 1 or chute >300):
            print ("Número inválido. Por favor informe um número de 1 a 100.")
            continue
        elif (chute == numero_secreto):
            print("Parabéns, resposta Certa! \n")
            print(f"Você fez {pontos} pontos.")
            break
        elif (chute < numero_secreto):
            print("Resposta errada.\nO número a ser adivinhado é maior!")
            if(rodada == numero_de_tentativas):
                print("Você já usou todas as suas chances. O numero secreto era: {}.".format(numero_secreto))
        else:
            print ("Resposta errada.\nO número a ser adivinhado é menor!")
            if(rodada == numero_de_tentativas):
                print("Você já usou todas as suas chances. O numero secreto era: {}.".format(numero_secreto))
        
        rodada += 1
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

    print("\nFim de Jogo.")

if(__name__ == "__main__"):
    jogar()

