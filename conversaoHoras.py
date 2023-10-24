numero = float(input("Digite um número de horas: "))

horas = numero
print("Horas:", horas)

dias = horas / 24
print("Dias:", dias)

minutos = horas * 60
print("Minutos:", minutos)

segundos = minutos * 60
print("Segundos:", segundos)

print("Conversão: {0:.0f} dia(s), {1:.0f} horas, {2:.2f} minutos e {3:.1f} segundos".format(dias, horas, minutos, segundos))