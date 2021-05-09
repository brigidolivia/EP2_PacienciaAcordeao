#Criando um baralho, só que agora de ordem aleatória: 
import random
def cria_baralho():
    naipes=['♠','♥','♦','♣']
    n=["2","3","4","5","6","7","8","9","10",'J','Q','K',"A"]
    mesa=[]
    i=0
    while i<len(naipes):
        i2=0
        while i2<len(n):
            mesa.append(n[i2]+naipes[i])
            i2+=1
        i+=1
    #Random shuffle- Ela altera o valor por referencia, ou seja, altera direto na fonte, o endereço de memória(Diferente do que vc viu até o momento)
    random.shuffle(mesa)   
    return mesa #['6♥','J♥','9♣','9♥']- Jogo Rápido para teste

#Encontrando o naipe
def extrai_naipe(x): 
    numero_naipe=str(x)
    naipe=numero_naipe[-1]
    return naipe

#Encontrando o valor
def extrai_valor(x):
    numero_naipe=str(x)
    valor=numero_naipe[0:-1]
    return valor

#Retornando as possibilidades
def lista_movimentos_possiveis(lista,i):
    possibilidades=[]
    if i==0:
        return possibilidades

    escolhida=lista[i]
    anterior=lista[i-1]

    if extrai_valor(escolhida)==extrai_valor(anterior) or extrai_naipe(escolhida)==extrai_naipe(anterior)  :
        possibilidades.append(1)

    if i==2 or i==1:
        return possibilidades
        
    terceira_anterior=lista[i-3]

    if extrai_valor(escolhida)==extrai_valor(terceira_anterior) or extrai_naipe(escolhida)==extrai_naipe(terceira_anterior):
        possibilidades.append(3)

    return possibilidades

#Empilha
def empilha(mesa, indice_escolhido, indice_substituido):
    mesa_atualizada=mesa
    mesa_atualizada[indice_substituido]=mesa_atualizada[indice_escolhido]
    del(mesa_atualizada[indice_escolhido])
    return mesa_atualizada

#Possibilidades
def possui_movimentos_possiveis(mesa):
    possibilidades=0
    for i in range (0,len(mesa)):
        escolhida=mesa[i]
        if i==0:
            possibilidades=possibilidades

        elif i!=0:
            anterior=mesa[i-1]
            if extrai_valor(escolhida)==extrai_valor(anterior) or extrai_naipe(escolhida)==extrai_naipe(anterior):
                possibilidades+=1

        elif i!=2 or i!=1:
            terceira_anterior=mesa[i-3]
            if extrai_valor(escolhida)==extrai_valor(terceira_anterior) or extrai_naipe(escolhida)==extrai_naipe(terceira_anterior):
                possibilidades+=1
    
    if possibilidades==0:
        return False
    else:
        return True

#INPUT PRA VALIDAR STRING NO IMPUT:
def peganumerodacarta(textoexibicaodoinput, mesa):
    #Modo de validar (vi no stackoverflow)
    numero_valido = False
    while not numero_valido:
        try:
            valor_entrada = int(input(textoexibicaodoinput))
            tamanhomesa = len(mesa)
            if valor_entrada<1 or valor_entrada>tamanhomesa:
                print("O número digitado sai do tamanho de seu baralho atual")
                numero_valido = False
            else:
                numero_valido=True
        except ValueError:
            print("O que foi digitado não é um numero inteiro válido.")
    return valor_entrada-1 #PQ -1? Pq o meu indice começa no zero, mas o de exibição começa no 1