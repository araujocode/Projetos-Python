ano = 1000

while ano <= 2024:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} É bissexto")
    ano += 1