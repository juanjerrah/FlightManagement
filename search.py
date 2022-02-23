# Desenvolvido por:
#                 JUAN JERRAH BARRETO DE OLIVEIRA
#                 RAPHAEL RODRIGUES DE SENA

import os
import lib
from distance import Distance

class Routes:
  vet = []
  caminhos = []
  correspondencias = []

  def __init__(self,raiz):
    self.raiz = raiz
  
  def check_road(self,node,destino):
    self.vet.append(node)
    res = 0
    if(node.destino != destino):
      if (node.direita != None):
        res += self.check_road(node.direita,destino)
      if (node.esquerda != None):
        res += self.check_road(node.esquerda,destino)
    else:
      self.caminhos.append(Route(self.vet.copy()))
      self.vet.clear()
      res += 1
    if (len(self.vet) != 0):
      self.vet.pop()
    return res

  def search(self,origem,destino):
    self.correspondencias.clear()
    self.clear_buffers()
    self.buscaGeral(self.raiz, origem)
    origens = []
    origens = self.correspondencias.copy()
    self.correspondencias.clear()

    for i in origens:
      if (lib.loop_busca(i,destino) == None):
        continue
      
      res = self.check_road(i,destino)
    
    for i in self.caminhos:
      if (i.trajeto[0].origem != origem):
        i.trajeto.pop(0)
      for j in i.trajeto:
        i.distance.insert(j.distancia)
      i.totalDistance()

    return res
        
  def clear_buffers(self):
    self.vet.clear()
    self.correspondencias.clear()
    self.caminhos.clear()

  def isCaminhos(self):
    return self.caminhos == []

  def print_caminhos(self):
    try:
      for route in self.caminhos:
        print("*"*35)
        print(f"{route.numTrajetos() - 1} Escala(s):")
        for voo in route.trajeto:
          voo.printVoo()
        print(f"Distancia Total: {route.total}")
        print("-"*35)
    except:
      print("Não há caminhos!")

  def buscaGeral(self,raiz,busca):
    if(raiz.destino == busca):
      self.correspondencias.append(raiz)
    if (raiz.direita != None):
      self.buscaGeral(raiz.direita,busca)
    if (raiz.esquerda != None):
      self.buscaGeral(raiz.esquerda,busca)

  def busca(self,origem,destino):
    self.caminhos.clear()
    self.correspondencias.clear()
    self.buscaGeral(self.raiz,origem)
    #self.correspondencias.pop(0)
    for i in self.correspondencias:
      self.search(i,i,origem,destino)
        
  def ordenarDistancia(self):
    os.system("cls")
    self.print_caminhos()
    print("*"*30)
    print("-"*30)
    print("Melhor opção: ")
    for voo in min(self.caminhos).trajeto:
      voo.printVoo()

class Route:
  trajeto = []
  total = 0
  def __init__(self,trajeto):
    self.distance = Distance()
    self.trajeto = trajeto

  def __eq__(self,obj):
    return self.total == obj.total
  
  def __lt__(self,obj):
    return self.total < obj.total
  
  def __gt__(self,obj):
    return self.total > obj.total
  
  def __ge__(self,obj):
    return self.total >= obj.total
  
  def __le__(self,obj):
    return self.total <= obj.total

  def totalDistance(self):
    self.total = self.distance.totalDistance()
  
  def numTrajetos(self):
    return len(self.trajeto)

  def bestRoute(self,obj):
    return self.total <= obj.total32