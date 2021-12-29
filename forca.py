import random

def jogar():

    print("********************************************")
    print("***Bem vindo ao jogo da Forca das Frutas!***")
    print("********************************************")

    palavra_secreta = carrega_palavra_secreta() # declarar a palavra_secreta que veio do return
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) # define parametro que vai usar palavra_secreta dentro lestras_acertadas por conta do escoplo de funções

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print("Ops, você errou! Faltam {} tentativas.".format(7-erros))

        enforcou = erros == 7 # na setima tentativa é game over
        acertou = "_" not in letras_acertadas # se não possuir "_" em palavras acertadas ganha o jogo
        print(letras_acertadas)

    if(acertou):
        print("GANHOU !!")
    else:
        print("PERDEU !!")
        print("A Fruta sorteada era: {} ".format(palavra_secreta))

def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip() #exclui o /n no final
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta # necessario colocar que vai retornar a palavra_secreta na função para carregar corretamente

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta] #List-Comprehensions

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper() # remove os espaços e verifica letras maiusculas e minusculas
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    
    index = 0
    for letra in palavra_secreta:
        if(chute == letra): 
            letras_acertadas[index] = letra
        index += 1  #index = index + 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()