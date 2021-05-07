from funcoes import *
from design import *
input('Quer jogar?')
mesa= cria_baralho()
pare=False
while not pare:
    print_estilizado(mesa)
    cartaescolhida=peganumerodacarta("Qual posição a sua carta escolhida está?")
    if mesa ==1:
        r= input ("Você ganhou, bora de novo?(s/n")
        if r=='s':
            pare=False
        else:
            print("Beleza! Talvez numa próxima!")
            pare=True

    elif possui_movimentos_possiveis(mesa)==0:
        r= input ("Você perdeu, aceita revanche?(s/n)")
        if r=='s':
            pare=False
        else:
            print("Beleza! Talvez numa próxima!")
            pare=True

    movimentos= lista_movimentos_possiveis(mesa, cartaescolhida)
     
    #Acho que essa parte pode virar função
    while movimentos==[]:
        cartaescolhida= peganumerodacarta('Vish, carta inválida. Escolha outra:')
        movimentos= lista_movimentos_possiveis(mesa, cartaescolhida)
    
    if movimentos==[1,3]:
        anterior=cartaescolhida-1
        terceira_anterior=cartaescolhida-3
        posicao_escolhida= peganumerodacarta("Duas possibilidades! {} ou {}?".format((anterior+1), (terceira_anterior+1)))
        while posicao_escolhida!=anterior and posicao_escolhida!=terceira_anterior:
            posicao_escolhida= peganumerodacarta("Inválido. Só duas possibilidades! {} ou {}?".format(anterior+1, terceira_anterior+1))
        if posicao_escolhida==anterior:
            mesa= empilha(mesa, cartaescolhida, anterior)
        elif posicao_escolhida==terceira_anterior:
            mesa= empilha(mesa, cartaescolhida, terceira_anterior)
        
        
    if movimentos==[1]:
        anterior=cartaescolhida-1
        mesa= empilha(mesa, cartaescolhida, anterior)
        
    if movimentos==[3]:
        terceira_anterior= cartaescolhida-3
        mesa= empilha(mesa, cartaescolhida, terceira_anterior)
print("isso ta após o while")



        
    
    
    