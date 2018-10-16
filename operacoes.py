menu = '''(1) - Média entre os números digitados
(2) - Diferença do maior pelo menor
(3) - Produto entre os números digitados
(4) - Divisão do primeiro pelo segundo'''

print("Informe dois números")
n1 = float(input())
n2 = float(input())

print(menu)
opt = input("Opção: ")

if opt == '1':
  print((n1+n2)/2) 
elif opt == '2':
  print(max(n1,n2) - min(n1,n2))
elif opt == '3':
  print(n1*n2)
elif opt == '4':
  print(n1/n2)
else:
  print("Opção inválida!")
