n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
n3 = int(input("Informe agora um terceiro valor inteiro: "))

if n1 < n2 and n1 > n3:
  print("O maior valor entre os três números é: ", n1)
if n2 > n1 and n2 > n3:
  print("O maior valor entre os três números é: ", n2)
else:
  print("O maior valor entre os três números é: ", n3)
