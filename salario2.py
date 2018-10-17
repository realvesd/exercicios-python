salario = float(input("Informe o valor do seu salário: "))

if salario < 300.00:
  novosalario = (salario * 1.45) + salario
elif 300.00 <= salario <= 600.00:
  novosalario = (salario * 1.25 ) + salario
else:
  novosalario = (salario * 1.15) + salario

print("O valor do salário reajustado é de R$ ", novosalario)
