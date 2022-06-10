#---------------------------------#
from Funções import hello

hello()
#---------------------------------#
from Funções import maior

maior(4, 7)
#---------------------------------#
from Funções import soma
#váriavel local recebendo valor -> total = 10
total = 10
#chamada do módulo soma de Funções usando sua váriavel
soma(3, 5)
#impressão da váriavel local do programa principal
print("Total principal = ", total)
print("\n\n")
#---------------------------------#
import Funções

s = Funções.soma3(3, 5)
print("Soma = ", s)
print("\n\n")
#----------------------------------#
j = Funções.calcula_juros(500,20)
print("O juros é = ", j)
print("\n\n")
#-----------------------------------#
print("Resposta do Exercício 01\n")
from Ex_Funções import linha
linha(50)
print("\n\n")
print("\nResposta do exercício 02\n")

from Ex_Funções import imprime_lista
L = [3,6,8,9,10,9,8,4]
imprime_lista(L)

print("\n\n")
#-----------------------------------#
import Estrutura_de_decisão
print(Estrutura_de_decisão)

import Ex_Estru_decisão
print(Ex_Estru_decisão)

import Estrutura_de_repetição
print(Estrutura_de_repetição)

import Ex_Estru_repetição
print(Ex_Estru_repetição)
