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
#Encontrando