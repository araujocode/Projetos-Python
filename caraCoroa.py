import random

escolha = random.choice(["cara", "coroa"])

num1 = int(input("Digite um número de 0 a 10: "))
num2 = int(input("Digite outro número de 0 a 10: "))

if escolha == "cara":
    if num1 < num2:
        print("O jogador que escolheu o numero", num1,"venceu")
    elif num2 < num1:
        print("O jogador que escolheu o numero", num2,"venceu")
    else:
        print("Os numeros escolhidos foram iguais")        
    #numero menor vence

if escolha == "coroa":
    if num1 > num2:
        print("O jogador que escolheu o numero", num1,"venceu")
    elif num2 > num1:
        print("O jogador que escolheu o numero", num2,"venceu")
    else:
        print("Os numeros escolhidos foram iguais")    
    #numero maior vence

print(escolha, "foi escolhido")