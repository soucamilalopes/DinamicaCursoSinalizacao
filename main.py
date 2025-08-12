#
#Sinalizacao
#

#criacao da classe sign que abre o arquivo de sinalização
class Sign:
  def __init__(self):
    self.f = open("sinalizacao.csv")

 #criação do método Extrair para os dados do arquivo
  def Extrair(self):
    f = self.f
    #criação da variável antiga para armazenar a data mais antiga
    antiga = ''
    #variável que pula o cabeçalho
    primeira = True
    #criação da variável ausentes para para armazenar os registros que não possuem latitude e longitude
    ausentes = []
    #criação do laço que percorre o arquivo e armazena os dados nas variáveis
    for line in f:
      #verifica se é a primeira linha e pula em caso positivo. Se não for, ele continua a excução
      if primeira:
        primeira = False
        continue
      #criação da variável lista que armazena os registros, tirando as quebras de linha e separa por ponto e vírgula
      lista = line.strip().split(';')
      #verifica se a variável antiga está vazia ou se a data da variável antiga é maior que a data da variável lista. É feita a indicação da posição da data na lista. Se uma das condições for verdadeira, ele armazena a data mais antiga na variável antiga.
      if antiga == '' or antiga > lista[4]:
        antiga = lista[4]
        #verifica se as colunas de latitude e longitude estão vazias. Se estiverem, é armazenado os registros na variável ausente.
      if lista[13].strip() == '' or lista[14].strip() == '':
        ausentes.append(lista)
      #else:
       #print(lista)

    return antiga, ausentes

#criação do objete e chamada do método Extrair
sign = Sign()
antiga = sign.Extrair()
ausentes = sign.Extrair()

#impressão no console dos resultados dos objetos
print("Antiga:", antiga)
print("Ausentes:", ausentes)
