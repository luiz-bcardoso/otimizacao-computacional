import re #expressao regular (regular expression)

nomesVariaveis = {} #dicionario com o nome das variaveis

matrizCoef = []#lista de coeficientes de todas variaveis

def determDiagPrinc(matrizCoef):
  for i in range(len(matrizCoef)):
    for j in range(len(matrizCoef)):
      print(matrizCoef[i][j])
  return matrizCoef

def recalculaLinha(linha,valorDiagonal):
  tamanho = len(linha)
  idx = 0
  while idx < tamanho:
    linha[idx] = round(linha[idx]/valorDiagonal, 2) ## arredonda valor para duas casas depois da vírgula
    idx+=1
  return linha


def valorDiagonal(matriz):
  linhas = len(matriz)
  indLinhas = 0
  indCoef = 0
  nrCoef = len(matriz[0])
  print()
  while indLinhas < linhas:
    while indCoef < nrCoef-1: #tira 1 pq é o LD (resultado)
      #testa se o valor é a diganal principal
      if(indLinhas == indCoef):
        valorDiagonal = matriz[indLinhas][indCoef]
      indCoef+=1
    #Termina de ler os valores da linha
    linha = matriz[indLinhas]
    matriz[indLinhas] = recalculaLinha(linha, valorDiagonal)
    indCoef = 0
    print(matriz[indLinhas] )
    indLinhas += 1


def retornaCoeficiente(linha,pos):
  valor=[]
  pc = pos-1
  while pc>=0: 
    if linha[pc]=='+' or linha[pc]=='-':
      if linha[pc]=='-':
        valor.append(linha[pc])#fez append com o '-'
        if len(valor)==1:
          #valor.append('1')
          valor.insert(0,'1')
          #valor.append('-')
          #break
        break
      else:
        if len(valor)==0:
          valor.append('1')
        break
    valor.append(linha[pc])
    pc=pc-1 #andar para a esquerda
  print(valor)
  valor.reverse()
  return ''.join(valor)

def insereVariavel(variavel):
  if variavel not in nomesVariaveis:
    nomesVariaveis[variavel]='sim'

def separaCoef_var(termo):
  coef = ''
  variavel = ''
  indice=0
  for letra in termo:
    if(letra.isdigit()):
      coef=coef+letra
      indice+=1 #incrementa o indice
    else:
      if indice==0: #a primeira letra nao eh um numero
        coef='1'
      variavel = termo[indice:]
      break #sai do for
  return coef,variavel

#monta um vetor com os coeficientes das keys a partir da linha
def montaCoeficientes(linha_entrada):
  nv = nomesVariaveis.keys()
  #vamos procurar cada nome de variavel em TODAS as linhas
  lista_dos_coeficientes = []                                 ##Lista com os coeficiente de cada variável.
  for nomeV in nv:#cada nome de variavel entre todas.
    pos = linha_entrada.find(nomeV)
    coef = -100
    if pos<0:#nome variavel nao encontrado na linha
      coef=0
    else:
      if pos==0:#nome variavel foi encontrado no inicio da linha
        coef=1
      else:
        if pos==1:#nome da variavel esta na posicao 1
          if linha_entrada[pos-1]=='-':
            coef = -1
          else:
            coef = float(linha_entrada[pos-1])
        else:#o nome da variavel esta na posicao >1
          #tratamento do coeficiente
          coef = retornaCoeficiente(linha_entrada,pos)
      lista_dos_coeficientes.append(float(coef))                ## Guarda cada coef. da equação em um vetor, ao dar append ele faz o cast para inteiro para não salvar como caracteres.
      print(nomeV,':',pos,' c:',coef)
  return lista_dos_coeficientes

def abre_arquivo(nomeArquivo):
  dados = open(nomeArquivo)
  for linha in dados:#percorre linha a linha o arquivo
    print(linha)
    linha = linha.rstrip()
    linha = linha.replace(' ','')#tira espaco em branco
    elementos = linha.split('=')#quebra a linha no igual
    le = elementos[0]
    ld = elementos[1]
    
    termos = re.split('-|\+',le)
    for termo in termos:
      if len(termo)>0:
        c,v = separaCoef_var(termo.lstrip().rstrip())
        insereVariavel(v)
      print('t:',termo)
    print(nomesVariaveis.keys())
    
    coeficientes = montaCoeficientes(linha)               ## Cria um vetor que usa o 'montaCoeficientes' para obter os coeficientes a cada iteração da equação.
    coeficientes.append(float(ld))                          ## Ao dar append, faz o cast para inteiro para não salvar como caracteres.
    matrizCoef.append(coeficientes)                       ## Faz o append de todos os coeficientes 

abre_arquivo('/workspaces/otimizacao-computacional/equacoes.txt')
c,v = separaCoef_var('x1')
print('Coeficiente:',c,'Variavel:',v)

print()


for linha in matrizCoef:                                ## Mostra a matriz com todos os coeficientes da equação mais o seu resultado.
  print(linha)
#determDiagPrinc(matrizCoef)
valorDiagonal(matrizCoef)