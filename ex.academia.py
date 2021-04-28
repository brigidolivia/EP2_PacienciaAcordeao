#Criando um baralho, só que agora de ordem aleatória:
import random
def cria_baralho():
    naipes=['♠','♥','♦',' ♣']
    n=["2","3","4","5","6","7","8","9","10",'J','Q','K',"A"]
    quatro=[]
    i=0
    while i<len(naipes):
        i2=0
        while i2<len(n):
            quatro.append(n[i2]+naipes[i])
            i2+=1
        i+=1
    return random.choices(quatro, k=len(quatro))
print(cria_baralho())

#Encontrando o naipe
def extrai_naipe(x):
    dois=str(x)
    naipe=dois[1]
    return naipe
print(extrai_naipe("A3"))

#Encontrando o valor
def extrai_valor(x):
    dois=str(x)
    valor=dois[0:-1]
    return valor
print(extrai_valor("A3"))