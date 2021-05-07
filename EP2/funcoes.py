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
    return mesa

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
def possui_movimentos_possiveis(lista):
    possibilidades=0
    for i in range (0,len(lista)):
        escolhida=lista[i]
        if i!=0:
            anterior=lista[i-1]
            if extrai_valor(escolhida)==extrai_valor(anterior) or extrai_naipe(escolhida)==extrai_naipe(anterior):
                possibilidades+=1

        if i!=2 or i!=1:    
            terceira_anterior=lista[i-3]
            if extrai_valor(escolhida)==extrai_valor(terceira_anterior) or extrai_naipe(escolhida)==extrai_naipe(terceira_anterior):
                possibilidades+=1
    
    if possibilidades==0:
        return False
    else:
        return True

#INPUT PRA INVALIDAR STRING NO IMPUT:
def try_input(textodoinput):
    
    #Modo de validar (vi no stackoverflow)
    numero_invalido = True
    while numero_invalido:
        try:
            valor_entrada = int(input(textodoinput))
            numero_invalido = False
        except ValueError:
            print("O que foi digitado não é um numero inteiro válido.")
    return valor_entrada
