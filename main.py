# Desenvolvido por:
#                 JUAN JERRAH BARRETO DE OLIVEIRA
#                 RAPHAEL RODRIGUES DE SENA

from flight import Flight as Voo
import os
import lib

hub = input("Digite o hub da empresa: ")
raiz = Voo(hub)
###Menu
while (True):
	os.system("cls")
	print("********* DESTINOS *********")
	lib.print_voos(raiz)
	print("*" * 15)
	print("1- Adicionar")
	print("2- Comprar Passagem")
	print("3- Sair")
	print("*" * 15)
	try:
		opc = int(input("Digite o valor correspondente: "))
	except:
		continue
	if (opc == 1):
		lib.adicionar_voo(raiz)
	elif (opc == 2):
		lib.comprar(raiz)
	elif (opc == 3):
		break
