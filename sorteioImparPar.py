import random

acertos = 0  
tentativas = 0

while acertos < 5:

    escolha = random.randint(0,100)
    print("O número foi escolhido")
    tentativas += 1

    imparPar = input("Você acha que o número sorteado é impar ou par? ").upper()

    if (imparPar == "PAR" and escolha % 2 == 0):
        print(f"Parabéns, você acertou. O número escolhido foi {escolha}\n")
        acertos += 1
        

    elif (imparPar == "IMPAR" and escolha % 2 != 0):
        print(f"Parabéns, você acertou. O número escolhido foi {escolha}\n")
        acertos += 1
        

    else:
        print(f"Você errou. O número escolhido foi {escolha}\n")
        

print(f"\nFim do jogo. Você acertou 5 vezes de {tentativas} tentativas.")       















"""""     
import random

acertos = 0

while acertos < 5:
    escolha = random.randint(0, 100)
    print("O número foi escolhido")

    imparPar = input("Você acha que o número sorteado é ímpar ou par? ")

    if (imparPar.upper() == "PAR" and escolha % 2 == 0) or (imparPar.upper() == "IMPAR" and escolha % 2 != 0):
        print(f"Parabéns, você acertou. O número escolhido foi {escolha}")
        acertos += 1
    else:
        print(f"Você errou. O número escolhido foi {escolha}")

"""

       

