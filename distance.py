# Desenvolvido por:
#                 JUAN JERRAH BARRETO DE OLIVEIRA
#                 RAPHAEL RODRIGUES DE SENA

class Distance:
  queue = []

  def __init__(self):
    None
  
  def insert(self,value):
    self.queue.append(value)

  def remove(self):
    if (len(self.queue) > 0):
      return self.queue.pop(0)
    else:
      return None
      
  def totalDistance(self):
    dis = 0

    while (True):
      res = self.remove()
      if(res == None):
        break
      
      dis = dis + res
    
    return dis
