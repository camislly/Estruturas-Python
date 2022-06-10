def hello():
    print("olá mundo!!!")
    # A definição dos parâmetros é opcional.
    print("\n")
#-------------------------------------------------#
def maior(x, y):
    if x > y:
        print(x)
    else:
        print(y)
        print("\n")
#------------------------------------------------#
def soma(x, y):
    total = x + y
    print("Total soma = ", total)
#-----------------------------------------------#
def soma2(x, y):
    global total2
    total2 = x + y
    print("Total soma2 = ", total2)
#--------------------------------------------------#
def soma3(x, y):
  total = x + y
  return total 
#--------------------------------------------------#
def calcula_juros(valor, taxa = 10):
  juros = valor*taxa/100
  return juros
  print("\n")
  
