import random

maquinaEscolha = random.choice(["pedra", "papel", "tesoura"])

usuarioEscolha = input("Escolha entre pedra, papel ou tesoura: ").lower()


if usuarioEscolha == "pedra":    
    print("Sua escolha foi:", usuarioEscolha)
    print("A máquina escolheu:", maquinaEscolha)

    if maquinaEscolha == "papel":
        print("Você perdeu. Papel ganha de tesoura")
    elif maquinaEscolha == "pedra":
        print("O jogo empatou")
    elif maquinaEscolha == "tesoura":
        print("Você ganhou. Pedra ganha de tesoura")

if usuarioEscolha == "papel":    
    print("Sua escolha foi:", usuarioEscolha)
    print("A máquina escolheu:", maquinaEscolha)

    if maquinaEscolha == "papel":
        print("O jogo empatou")
    elif maquinaEscolha == "pedra":
        print("Você ganhou. Papel ganha de pedra")
    elif maquinaEscolha == "tesoura":
        print("Você perdeu. Tesoura ganha de papel")

if usuarioEscolha == "tesoura":    
    print("Sua escolha foi:", usuarioEscolha)
    print("A máquina escolheu:", maquinaEscolha)

    if maquinaEscolha == "papel":
        print("Você ganhou. Tesoura ganha de papel")
    elif maquinaEscolha == "pedra":
        print("Você perdeu. Pedra ganha de tesoura")
    elif maquinaEscolha == "tesoura":
        print("O jogo empatou")





""""
import random

opcoes = ["pedra", "papel", "tesoura"]
maquinaEscolha = random.choice(opcoes)

usuarioEscolha = input("Escolha entre pedra, papel ou tesoura: ").lower()

print("Sua escolha foi:", usuarioEscolha)
print("A máquina escolheu:", maquinaEscolha)

resultados = {
    ("pedra", "papel"): "Você perdeu. Papel ganha de pedra",
    ("pedra", "tesoura"): "Você ganhou. Pedra ganha de tesoura",
    ("papel", "pedra"): "Você ganhou. Papel ganha de pedra",
    ("papel", "tesoura"): "Você perdeu. Tesoura ganha de papel",
    ("tesoura", "pedra"): "Você perdeu. Pedra ganha de tesoura",
    ("tesoura", "papel"): "Você ganhou. Tesoura ganha de papel",
}

if usuarioEscolha == maquinaEscolha:
    print("O jogo empatou")
else:
    resultado = resultados.get((usuarioEscolha, maquinaEscolha), "Escolha inválida")
    print(resultado)
"""