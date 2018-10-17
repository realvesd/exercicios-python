prod = str(input("Informe o código do produto: "))

if prod == '1' or prod == '2':
  classi = 'Sul'
elif prod == '3' or prod == '4':
  classi = 'Sudeste'
elif prod == '5' or prod == '6':
  classi = 'Norte'
elif prod == '7' or prod == '8':
  classi = 'Nordeste'
elif prod == '10' or prod == '11':
  classi = 'Centro-oeste'
else:
  print('Código inválido')

print("O produto ", prod, "vem da região ", classi)
