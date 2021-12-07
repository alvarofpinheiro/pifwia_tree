# Dados de entrada para arvore de decisao
entrada_a = [True, True, True, True, True, False, False, False, True, True]
entrada_b = [False, True, True, False, True, False, False, False, True, False]
saida = ['+', '+', '+', '-', '+', '-', '-', '-', '-', '-']

possiveis_entradas = [True, False]
possiveis_saidas = ['+', '-']

# Implementação de uma arvore binaria
class Arvore:
  def __init__(self, valor):
    self.valor = valor
    self.arvore_esquerda = 0
    self.arvore_direita = 0
  

# Calcular
def gini_origem(saidas, possibilidades):
  quantidade_de_cada_saida = [0]*len(possibilidades)

  for i in saidas:
    for j in range(0, len(possibilidades)):
      if i == possibilidades[j]:
        quantidade_de_cada_saida[j] += 1

  gini = 1
  for i in quantidade_de_cada_saida:
    gini -= (i/len(saidas))**2

  return gini

def ganho_entrada(entrada, possiveis_entradas, saidas, possiveis_saidas):
  quantidade_de_cada_saida = [0]*len(possiveis_entradas)*len(possiveis_saidas)

  for index, i in enumerate(entrada):
    for index_entrada, k in enumerate(possiveis_entradas):
      if i == k:
        for index_saida, j in enumerate(possiveis_saidas):
          if saidas[index] == j:
            quantidade_de_cada_saida[index_entrada*len(possiveis_saidas) + index_saida] += 1

  gini = [1, 0]*len(possiveis_entradas)
  indice = 0
  for i in range(0, len(quantidade_de_cada_saida), len(possiveis_saidas)):
    total = 0
    for j in range(0, len(possiveis_saidas)):
      gini[indice*2 + 1] += quantidade_de_cada_saida[i + j]
    for j in range(0, len(possiveis_saidas)):
      gini[indice*2] -= (quantidade_de_cada_saida[i + j]/gini[indice*2 + 1])**2
    indice += 1

  ganho = gini_origem(saida, possiveis_saidas)
  for i in range(0, int(len(gini)/2)):
    ganho -= gini[2*i] * (gini[2*i + 1]/len(entrada))
  return ganho

origem = gini_origem(saida, possiveis_saidas)
ganho_a = ganho_entrada(entrada_a, possiveis_entradas, saida, possiveis_saidas)
ganho_b = ganho_entrada(entrada_b, possiveis_entradas, saida, possiveis_saidas)

print('Gini Origem: ', origem)
print('Ganho usando entrada A como raiz: ', ganho_a)
print('Ganho usando entrada B como raiz: ', ganho_b)