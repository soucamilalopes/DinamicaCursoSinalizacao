#
#Sinalizacao
###

f = open("sinalizacao.csv")

for line in f:
  print(line.strip().split(';'))

