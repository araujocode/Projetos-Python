import re

nome = input("Digite o mes do seu aniversário: ")
pardaoMes = "r^[0-9]"

print("Boas vindas", nome)

mesNascimento = int(input(nome + ", qual o seu mês de nascimento? "))

mesNascimento = re.match(r"\b\w{5}")

signos = ["Aquário", "Peixes", "Áries", "Touro", "Gêmeos", "Cancer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio"]

opt = input("Digite uma opção: 1 - entrar, 2 - cadastrar, 3 - mostrar, 4 - sair")
if not opt == 4:
    print("Continuar no programa")
else:
    print("sair do programa")