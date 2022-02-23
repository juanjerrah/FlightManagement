# Desenvolvido por:
#                 JUAN JERRAH BARRETO DE OLIVEIRA
#                 RAPHAEL RODRIGUES DE SENA

class Flight:
  def inserir_direita(self, direita):
    self.direita = direita
    self.direita.origem = self.destino

  def inserir_esquerda(self, esquerda):
    self.esquerda = esquerda
    self.esquerda.origem = self.destino

  def __init__(self, destino):
    self.direita = None
    self.esquerda = None
    self.origem = None
    destino = destino.upper()
    self.destino = destino
    self.distancia = 0

  def setDistancia(self, distancia):
    self.distancia = distancia
    print()
  def isDestino(self,busca):
    return self.destino == busca
  def printVoo(self):
    if(self.origem != None):
      print(f'Origem   : {self.origem} Destino: {self.destino}')
      print(f'Distância: {self.distancia}')
      print("-" * 40)