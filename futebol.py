idade = str(input("Qual a idade do atleta? "))

if idade >= '05' and idade <= '10':
  classi = 'Infantil'
elif idade >= '11' and idade <= '15':
  classi = 'Juvenil'
elif idade >= '16' and idade <= '20':
  classi = 'Junior'
elif idade >= '21'and idade <= '25':
  classi = 'Profissional'
else:
  print("Idade não aceita!")

print("Se o atleta tiver ", idade, "anos, ele será classificado como ", classi)
