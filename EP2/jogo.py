input('Quer jogar?')
mesa= cria_baralho()
pare=False
while not pare:
    print(mesa)
    cartaescolhida=input("Qual posição a sua carta escolhida está?")
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

    movimentos= lista_movimentos_possiveis(cartaescolhida)

    else:
        if movimentos==0:
            movimentos= ('Vish, carta inválida. Escolha outra:')
    
        elif movimentos==[1,3]:
            anterior=mesa[cartaescolhida-1]
            terceira_anterior=mesa[cartaescolhida-3]
            posicao_escolhida= input("Duas possibilidades! {} ou {}?".format(anterior, terceira_anterior))
            if posicao_escolhida==anterior:
                mesa= empilha(mesa, cartaescolhida, anterior)
            elif posicao_escolhida==terceira_anterior:
                mesa= empilha(mesa, cartaescolhida, terceira_anterior)
        
        elif movimentos==[1]:
            anterior=mesa[cartaescolhida-1]
            mesa= empilha(mesa, cartaescolhida, anterior)
        
        else movimentos==[3]:
            terceira_anterior=mesa[cartaescolhida-3]
            mesa= empilha(mesa, cartaescolhida, terceira_anterior)




        
    
    
    