import random

maquinaEscolha = random.choice(["pedra", "papel", "tesoura"])

usuarioEscolha = input("Escolha entre pedra, papel ou tesoura: ").lower()


if usuarioEscolha == "pedra" and maquinaEscolha == "tesoura":
    print("Sua escolha foi:", usuarioEscolha)
    print("A máquina escolheu:", maquinaEscolha)
    print("Você venceu")
    if:
        print("Você perdeu")    

elif usuarioEscolha == "tesoura" and maquinaEscolha == "papel":
    print("Sua escolha foi:", usuarioEscolha)
    print("A máquina escolheu:", maquinaEscolha)
    print("Você venceu")   

elif usuarioEscolha == "papel" and maquinaEscolha == "pedra":
    print("Sua escolha foi:", usuarioEscolha)
    print("A máquina escolheu:", maquinaEscolha)
    print("Você venceu")
    