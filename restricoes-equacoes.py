# Trabalho em aula dado no dia 18/04, feito por Luiz Batista Cardoso, Matheus Braga e Matheus Faccin.
# Versão 3, ultima vez atualizado dia 05/09/2023.

#criar uma classe coeficiente angular e associar as retas ultilizadas para achar aquele coeficiente angular.
class Restricao():
    def __init__(self, cordenadaX , cordenadaY, coeficiente,sinal=None):
        self.cordenadaX = cordenadaX 
        self.cordenadaY = cordenadaY
        self.coeficiente = coeficiente
        self.sinal = sinal
        
    #calcula a intersecção da seguinte forma:
    #primeiro achamos o valor de x usando a seguinte formula " M1X1 + B1 = M2X2 + B2 "
    # que vai resulta em " M1X1-M2X2 = B2 -B1 " e por fim vai resultar em " X = B/M "
    # depois de acharmos o X eu subistitui o X na primeira equação no caso "M*valor de X + B"
class Pontos():

        def __init__(self, x , y,restricao1, restricao2=None):
            self.restricao1 = restricao1
            self.restricao2 = restricao2
            self.x = x 
            self.y = y
        
    
def calcularInterseccao(x1, y1, c1, x2, y2, c2):
    det = x1*y2 - x2*y1
    det_x = c1*y2 - c2*y1
    det_y = x1*c2 - x2*c1
    if det != 0:
        x = det_x / det
        y = det_y / det
        x = x*(-1)
        y = y*(-1)
        x = round(x,2)
        y = round(y,2)
        return (x, y)
    else:
        return 0 , 0

def acharInterseccao(coeficientes,pontos,restricoes):
    # i=0 < tamanho lista coeficientes i++ 
    # j= 0 < tamanho lista coeficientes j++
    for i in range(len(coeficientes)):
      print("contador: "+str(i)+" coeficiente: "+str(coeficientes[i]))
      for j in range(len(coeficientes)):
        print("contador: "+str(j)+" coeficiente: "+str(coeficientes[j]))
        #se o i tiver o mesmo valor que o j exemplo: i=1 e o j=1 ele vai pular para não comparar o mesmo valor
        if i == j:
          print("")
        # se o coeficiente na posição i da lista de coeficientes for igual ao coeficiente na posição j 
        # da lista de coeficientes significa que as retas são paralelas
        elif coeficientes[i] == coeficientes[j]:
          print("as retas são paralelas")
        
        # se os coeficientes forem diferentes significa que elas não são paralelas logo tem intercecção
        elif coeficientes[i] != coeficientes[j]:
            print("as retas não são paralelas")
            #calcula o ponto(x,y) da intercecção das retas
            x,y = calcularInterseccao(restricoes[i].cordenadaX,restricoes[i].cordenadaY,restricoes[i].coeficiente,restricoes[j].cordenadaX,restricoes[j].cordenadaY,restricoes[j].coeficiente,)          
            #verifica se o Ponto(x,y) ja foi adicionado na Lista de Pontos 
            if any(ponto.x == x for ponto in pontos) == True and any(ponto.y == y for ponto in pontos) == True:
                print("ponto ja adicionado")
            else:
                #depois de verificar que o ponto não foi adicionado ele adiciona na lista de pontos
                pontos.append(Pontos(x,y,restricoes[i],restricoes[j]))
        else:
            print("")

def coeficienteAngular(retas,coeficientes):
    
    # 2x+2y <=6
    # coeficiente angular  = x/y 2/2
    # x + 0 >= 0
    
        for reta in retas:
            if reta.cordenadaX == 0:
                resultado = ""
            elif reta.cordenadaY == 0 :
                resultado = ""
                
            else:
                resultado = reta.cordenadaX/reta.cordenadaY
            coeficientes.append(resultado)
            
            
def exibirPontos(pontos):
    for ponto in pontos:
        if ponto.restricao2==None:
            print("retrição 1: "+str(ponto.restricao1.cordenadaX)+"  "+str(ponto.restricao1.cordenadaY))
            print("x: "+str(ponto.x)+" y: "+str(ponto.y))
            
        else:
            print("retrição 1: "+str(ponto.restricao1.cordenadaX)+"  "+str(ponto.restricao1.cordenadaY)+"  "+str(ponto.restricao1.coeficiente))
            print("retrição 2: "+str(ponto.restricao2.cordenadaX)+"  "+str(ponto.restricao2.cordenadaY)+"  "+str(ponto.restricao2.coeficiente))
            print("x: "+str(ponto.x)+" y: "+str(ponto.y))
            
def calcularPontosRetas(restricoes,pontos):
    #percorre a lista de restrições 
    for restricao in restricoes:
        
        if restricao.cordenadaY!=0 and restricao.cordenadaX!=0:
            y = -(restricao.coeficiente/restricao.cordenadaY)
            x = -(restricao.coeficiente/restricao.cordenadaX)
            pontos.append(Pontos(x,0,restricao))
            pontos.append(Pontos(0,y,restricao))
                       
def calcularFuncaoObjetiva(pontos, resultado,xMax,yMax):
    #// Para calcular a função Max. basta aplicar junto a cada ponto, logo...
    
    #// 1) Transformar a função dada em equação.
    #// ex: 3x - y  --> 3.(x) - 1*(y), onde x e y pertencem ao ponto dado pelo limite.
    
    #// 2) Calcular Z para o coefiente de cada ponto.
    #// ex: xMax = 3 e yMax = -1 para 3x - 1y. 

    #// Para todos os pontos contido em pontos:
    for ponto in pontos:

        #// Exibe o resultado da função maximizar:
        print("Z Maximizado para o ponto P(",ponto.x,", ",ponto.y,"): \n")
        print("Z = (",xMax,"*",ponto.x,") + (",yMax,"*",ponto.y,")")

        #// M. Faccin disse que o python não sabe regra de sinal então tem que dividir em duas variaveis.
        a = (xMax*ponto.x)
        b = (yMax*ponto.y)
        resultado.append(-(a + b)) # (lista??)

    return resultado
        #// Imprime o resultado além de guardar em uma lista/array/tudo.
        


 

def acharPontosValidos(pontos, restricoes):
    pontosValidos = []
    for ponto in pontos:
        print("ponto x: ",ponto.x," y: ",ponto.y)
        contador = 0
        for restricao in restricoes:
            resultado = calculoPontosRestricoes(ponto,restricao)
            
            if restricao.coeficiente<=0:
                
                if restricao.sinal == "":
                    print("não tem restrição")
                elif eval(str(resultado)+restricao.sinal+str((-restricao.coeficiente))):
                    print("valido para ",resultado)
                    
                else:
                    print("invalido invalido para ",resultado)
                    contador+=1
                    
            else:
                print("algo errado")
        
        if contador==0:
            pontosValidos.append(ponto)
        else:
            contador = 0
    return pontosValidos
    
def calculoPontosRestricoes(ponto,restricao):
    #if restricao.cordenadaX == -1:
      #  restricao.cordenadaX = 1
    #if restricao.cordenadaY == -1:
       # restricao.cordenadaY = 1
    resultado = (ponto.x*restricao.cordenadaX)+(ponto.y*restricao.cordenadaY)
    resultado = round(resultado,2)
    return resultado


restricoes  = []
coeficientes = []
pontos = []
sistema = []
resultados = []
# input para o usuario escolher os valores das retas NÃO DIGITE LETRAS DIGITE APENAS VALORES 
numeroRetas = int(input("quantas restrições você quer criar ? "))
i = 0
while i < numeroRetas:        
    x = float(input("defina o valor de x da reta "+str(i+1)+" :  "))
    y = float(input("defina o valor de y da reta "+str(i+1)+" :  "))
    coeficiente = float(input("defina o valor do coeficiente da reta"+str(i+1)+" : "))
    sinal = input("digite o sinal do coeficiente ( >= , <= )")
    if coeficiente > 0:
        coeficiente = -coeficiente
        
    restricoes.append(Restricao(x,y,coeficiente,sinal))
    print("x: " +str(restricoes[i].cordenadaX) + "  y: "+ str(+restricoes[i].cordenadaY)+"  restrição: "+ str(+restricoes[i].coeficiente))
    i+=1
 
    
calcularPontosRetas(restricoes,pontos)
coeficienteAngular(restricoes,coeficientes)
print("numero de coeficientes: "+str(len(coeficientes)))
print("numero de restricoes: "+str(len(restricoes)))
acharInterseccao(coeficientes,pontos,restricoes)
print("pontos de intersecção ")
exibirPontos(pontos)

print("resultado do max")

xMaxima = float(input("digite o x da equação maxima"))
yMaxima = float(input("digite o y da equação maxima"))


pontosValidos = acharPontosValidos(pontos,restricoes)

for ponto in pontosValidos:
    print("x: ",ponto.x," y: ",ponto.y)
    
resultados = calcularFuncaoObjetiva(pontosValidos,resultados,xMaxima,yMaxima)
for resultado in resultados:
    print(str(-resultado))



