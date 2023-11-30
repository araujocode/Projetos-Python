import random

escolha = random.choice(["cara", "coroa"])

num1 = int(input("Digite um número de 0 a 10: "))
num2 = int(input("Digite outro número de 0 a 10: "))

if escolha == "cara":
    # numero menor vence
    if num1 < num2:
        print("O jogador que escolheu o numero", num1, "venceu")
    elif num2 < num1:
        print("O jogador que escolheu o numero", num2, "venceu")
    else:
        print("Os numeros escolhidos foram iguais")

if escolha == "coroa":
    # numero maior vence
    if num1 > num2:
        print("O jogador que escolheu o numero", num1, "venceu")
    elif num2 > num1:
        print("O jogador que escolheu o numero", num2, "venceu")
    else:
        print("Os numeros escolhidos foram iguais")


print(escolha, "foi escolhido")
