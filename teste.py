from datetime import date
anoAtual = date.today().year

nome = "Bruno"
anoNascimento = 1999
proxAno = (anoAtual - anoNascimento) + 1
idadeAnterior = (anoAtual - anoNascimento) - 10

print("Olá, meu nome é", nome, "e eu tenho", anoAtual - anoNascimento, "anos de idade")
print("Ano que vem eu faço", proxAno, "anos")
print("Há 10 anos atrás, eu tinha", idadeAnterior, "anos")
print("Eu nasci em", anoNascimento)









