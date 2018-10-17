menu = ''' (1) Informar o maior número
(2) Informar o menor número
(3) Relatar erro do código'''

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe o segundo valor inteiro: "))

print(menu)
codigo = (str(input("Informe o código da operação desejada: "))

if codigo == '1':
  ope = max(n1,n2)
elif codigo =='2':
  ope = min(n1,n2)
elif codigo == '3':
  print('Erro no código')
else:
  print("Código não existe")
