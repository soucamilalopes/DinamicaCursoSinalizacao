#
#Sinalizacao
#

class Sign:
  def __init__(self):
    self.f = open("sinalizacao.csv")

  def Extrair(self):
    f = self.f
    antiga = ''
    primeira = True
    ausentes = []
    for line in f:
      if primeira:
        primeira = False
        continue
      lista = line.strip().split(';')
      if antiga == '' or antiga > lista[4]:
        antiga = lista[4]
      if lista[13].strip() == '' or lista[14].strip() == '':
        ausentes.append(lista)
      else:
       print(lista)

    return antiga, ausentes

sign = Sign()
antiga = sign.Extrair()
ausentes = sign.Extrair()

print("Antiga:", antiga)
print("Ausentes:", ausentes)
