import random

def jogar():

    print("\n\n")
    print ("Bem vindo ao jogo da forca.")
    print("\n")

    frutas = []

    with open("Frutas_sem_caracteres_especiais.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip().lower()
            frutas.append(linha)

    
    palavra_secreta = random.choice(frutas)

    print('\n')
    print (palavra_secreta)
    print('\n')
    
    enforcado = False
    acertou = False
    numero_da_tentativa = 1                                                

    print ("Informe o nível de dificuldade desejada")
    print("1 (Fácil)     2 (Médio)     3 (Difícil)")
    nivel_dificuldade = int(input("\nQual é o nível de dificuldade desejado?"))

    if (nivel_dificuldade == 1):
        tentativas = len(palavra_secreta) + 7
    elif (nivel_dificuldade == 2):
        tentativas = len(palavra_secreta) + 5
    else:
        tentativas = len(palavra_secreta)+ 3

    # Colocando um '_' para cada letra da palavra secreta
        
    lista = ["_" for letra in palavra_secreta]
    
    print ('\n')
    print (lista)

    # início do loop:

    while((enforcado == False) and (acertou == False)):
        
        index = 0                                                               # se o index for declarado antes do while retornará a posição errada.
        chute = (input("\nDigite uma letra:")).lower().strip()
        for letra in palavra_secreta:
            if (letra == chute):
                lista.pop(index)                                            # Retira o '_' na posição indicada e na linha abaixo é substituida pela letra correspondente.
                lista.insert(index, chute)
            index = index + 1

        if(lista.count("_")) == 0:
            print(f"\nTentativa {numero_da_tentativa}/{tentativas}")
            print(lista)
            print("\nParabéns! Você acertou a palavra.")
            break
        elif(numero_da_tentativa == tentativas) and ((lista.count("_")) != 0):
            print(f"\nTentativa {numero_da_tentativa}/{tentativas}")
            print(lista)
            print("Você foi enforcado!!!")
            print (f"A palavra secreta era {palavra_secreta}.")
            break
        else:
            print(f"\nTentativa {numero_da_tentativa}/{tentativas}")
            print(lista)
        numero_da_tentativa = numero_da_tentativa + 1

            
    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()