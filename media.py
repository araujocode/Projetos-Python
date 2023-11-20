nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota do bimestre: "))
nota2 = float(input("Digite sua segunda nota do bimestre: "))
nota3 = float(input("Digite sua terceira nota do bimestre: "))
nota4 = float(input("Digite sua quarta nota do bimestre: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(nome, "sua média final é:", media)

if media < 7:
    print("Você foi reprovado")
else:
    print("Você foi aprovado")
