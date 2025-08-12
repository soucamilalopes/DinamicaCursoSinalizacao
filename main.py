#
#Sinalizacao
#

f = open("sinalizacao.csv")


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
  
  
print(antiga)
print(ausentes)