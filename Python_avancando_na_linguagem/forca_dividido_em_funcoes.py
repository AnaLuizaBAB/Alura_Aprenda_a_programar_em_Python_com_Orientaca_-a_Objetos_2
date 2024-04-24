import random

    
def func_escolhe_palavra_secreta():

    frutas = []

    with open("Frutas_sem_caracteres_especiais.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip().lower()
            frutas.append(linha)

    palavra_secreta = random.choice(frutas)

    return palavra_secreta

def func_nivel_dificuldade():
    
    print ("Informe o nível de dificuldade desejada")
    print("1 (Fácil)     2 (Médio)     3 (Difícil)")
    nivel_dificuldade = int(input("\nQual é o nível de dificuldade desejado?"))

    while ((nivel_dificuldade != 1) and (nivel_dificuldade != 2) and (nivel_dificuldade != 3)):
        print ("\nNível de dificuldade invalido.")
        print ("\n\nInforme o nível de dificuldade desejada")
        print("1 (Fácil)     2 (Médio)     3 (Difícil)")
        nivel_dificuldade = int(input("\nQual é o nível de dificuldade desejado?"))
    return nivel_dificuldade

def func_esqueleto_palavra_secreta(palavra):

    # Colocando um '_' para cada letra da palavra secreta
        
    lista = ["_" for letra in palavra]

    return lista

def func_numero_tentativas(nivel, palavra):

    if (nivel == 1):
        tentativas = len(palavra) + 5
    elif (nivel == 2):
        tentativas = len(palavra) + 4
    else:
        tentativas = len(palavra)+ 2

    return tentativas

def func_desenho_perdedor():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def func_desenho_ganhador():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def jogar():

    print("\n\n")
    print ("Bem vindo ao jogo da forca.")
    print("\n")

    nivel_dificuldade = func_nivel_dificuldade()

  
    palavra_secreta = func_escolhe_palavra_secreta()
    lista = func_esqueleto_palavra_secreta(palavra_secreta)
    tentativas = func_numero_tentativas(nivel_dificuldade, palavra_secreta)
    
    enforcado = False
    acertou = False
    numero_da_tentativa = 1                                               

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
            print("\nParabéns! Você acertou a palavra.\n")
            func_desenho_ganhador()
            break
        elif(numero_da_tentativa == tentativas) and ((lista.count("_")) != 0):
            print(f"\nTentativa {numero_da_tentativa}/{tentativas}")
            print(lista)
            print (f"\nA palavra secreta era {palavra_secreta}.")
            print("Você perdeu!\n")
            func_desenho_perdedor()
            break
        else:
            print(f"\nTentativa {numero_da_tentativa}/{tentativas}")
            print(lista)
        numero_da_tentativa = numero_da_tentativa + 1

            
    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()