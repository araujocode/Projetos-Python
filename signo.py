nome = input("Digite seu nome: ")
print("Boas vindas", nome)

mesNascimento = int(input(nome + ", qual o seu mês de nascimento? "))

if mesNascimento == 1 & mesNascimento == "janeiro".upper():
    print(nome, "seu signo é aquário")
elif mesNascimento == 2 | mesNascimento == "fevereiro".upper():
    print(nome, "seu signo é Peixes")
elif mesNascimento == 3 or mesNascimento == "marco".upper():
    print(nome, "seu signo é Áries")
elif mesNascimento == 4 or mesNascimento == "abril".upper():
    print(nome, "seu signo é Touro")
elif mesNascimento == 5 or mesNascimento == "maio".upper():
    print(nome, "seu signo é Gêmeos")
elif mesNascimento == 6 or mesNascimento == "junho".upper():
    print(nome, "seu signo é Câncer")
elif mesNascimento == 7 or mesNascimento == "julho".upper():
    print(nome, "seu signo é Leão")
elif mesNascimento == 8 or mesNascimento == "agosto".upper():
    print(nome, "seu signo é Virgem")
elif mesNascimento == 9 or mesNascimento == "setembro".upper():
    print(nome, "seu signo é Libra")
elif mesNascimento == 10 or mesNascimento == "outubro".upper():
    print(nome, "seu signo é Escorpião")
elif mesNascimento == 11 or mesNascimento == "novembro".upper():
    print(nome, "seu signo é Sagitário")
elif mesNascimento == 12 or mesNascimento == "dezembro".upper():
    print(nome, "seu signo é Capricórnio")
else:
    print("Digite um mês válido, entre 1 e 12")


