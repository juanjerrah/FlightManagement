# Desenvolvido por:
#                 JUAN JERRAH BARRETO DE OLIVEIRA
#                 RAPHAEL RODRIGUES DE SENA

from flight import Flight as Voo
import os
from search import Routes as Caminho

def input_cidade(text):
  return input(text).upper()
  
def print_voos(inicio):
	if (inicio.origem != None):
		inicio.printVoo()
	if (inicio.direita != None):
		print_voos(inicio.direita)
	if (inicio.esquerda != None):
		print_voos(inicio.esquerda)


def loop_busca(inicio, busca):
	if (inicio.isDestino(busca) == True):
		return inicio
	else:
		if (inicio.direita != None):
			res = pesquisa(inicio.direita, busca)
			if (res != None):
				return res
			else:
				if (inicio.esquerda != None):
					res = pesquisa(inicio.esquerda, busca)
					if (res != None):
						return res
					else:
						return None


def pesquisa(inicio, busca):
	busca = busca.upper()
	return loop_busca(inicio, busca)
    
def novo_voo(origem, novo):
	if (origem.direita == None):
		origem.inserir_direita(novo)
	elif (origem.esquerda == None):
		if (origem.direita.distancia > novo.distancia):
			temp = origem.direita
			origem.inserir_direita(novo)
			origem.inserir_esquerda(temp)
		else:
			origem.inserir_esquerda(novo)
	else:
		return -1
	return 0


def adicionar_voo(malha):
  os.system("cls")
  res = Caminho(malha)
  
  quit = False
  while(quit == False):
    while (True):
      origem = input_cidade("Digite a origem do voo:")
      res.buscaGeral(malha,origem)
      if (len(res.correspondencias) != 0):
        break
      else:
        res.correspondencias.clear()
        print("Origem não registrada na malha da empresa!")
    dest = input_cidade("Digite o destino: ")
    add = Voo(dest)
    try:
      distancia = int(input("Digite a distância do voo: "))
    except:
      print("Valor inválido!!!")
      continue
    add.setDistancia(distancia)
    
    for i in res.correspondencias:
      if(novo_voo(i,add) == 0):
        quit = True
        break
    else:
      print("Não foi possível associar o novo voo a um nó/escala!")

    res.correspondencias.clear()
  
def comprar(raiz):
  origem = input("Digite a origem: ")
  origem = origem.upper()
  pOrigem = pesquisa(raiz,origem)
  if(pOrigem == None):
    return
  destino = input("Digite o destino: ")
  destino =  destino.upper()
  pDestino = pesquisa(raiz,destino)
  if (pDestino == None):
    return
  
  options = Caminho(raiz)
  res = options.search(origem,destino)
  print(f"Existem {res} opções possíveis em nossa malha!")

  options.ordenarDistancia()
  input("...")
  