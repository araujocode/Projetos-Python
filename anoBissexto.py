import random

def function(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é bissexto")


for ano in range(1400,1800):
    function(ano)
