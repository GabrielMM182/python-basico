import random

def jogar(): # cria a função jogar para poder rodar e chamar tambem no 'jogos'

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101) #num e vai pegar de 1 ate 100
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) -> Fácil (2) -> Médio (3) -> Difícil")

    nivel = int(input("Define o nível:"))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 3
    else:
        print("opção de nivel invalida, favor escolher um nivel correto")

    for rodada in range(0, total_tentativas): # vai começar a contar de 0 ate o num escolhido
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)

        chute = int(chute_str)  # vai passar o string para int

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute) # abs vai retornar o valor absoluto
            pontos = pontos - pontos_perdidos           

    print("Fim do jogo")
    print("o numero gerado foi", numero_secreto)

if (__name__ == "__main__"): # verifica o nome do arquivo para poder rodar separadamente no cmd
    jogar()
