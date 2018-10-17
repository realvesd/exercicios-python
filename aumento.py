valor = float(input("Qual o preço do produto? "))
if valor <= 50.00:
  valor = valor * 1.05
elif 50.00 < valor <= 100.00: 
  valor = valor * 1.10
else:
  valor = valor * 1.15

if valor <= 80.00:
  classi = 'Barato!'
elif 80.00 < valor <= 120.00:
  classi = 'Valor normal!'
elif 120.00 < valor <= 200.00:
  classi = 'Caro!'
else:
  classi = 'Muito caro!'

print("O novo valor é ", valor, "classificado como ", classi)
