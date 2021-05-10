from funcoes import *
from design import *

print("Olá! Bem vindo ao Barzin da esquina. Aqui sempre tem alguém jogando baralho")
input("Olha lá! Tem gente jogando Acordeão. Quer se juntar? Eu te explico as regras (APERTE ENTER)")

#COLOCAR TEXTO AQUI
with open ("EP2_PacienciaAcordeao.py/EP2/textodojogo.txt",'r',encoding='utf8') as instrucoes:#encoding='utf8'- Aceitar acentos. padrão-inglês UNICODE-Mais memória, mais variedade
    texto= instrucoes.read()
print(texto)

input("Agora sim! Aperte Enter para começar")
mesa= cria_baralho()

pare=False
while not pare:
    print_estilizado(mesa)
    cartaescolhida=peganumerodacarta("Qual posição a sua carta escolhida está?", mesa)
    
    movimentos= lista_movimentos_possiveis(mesa, cartaescolhida)
     
    #Acho que essa parte pode virar função
    while movimentos==[]:
        cartaescolhida= peganumerodacarta('Vish, carta inválida. Escolha outra:', mesa)
        movimentos= lista_movimentos_possiveis(mesa, cartaescolhida)
    
    if movimentos==[1,3]:
        anterior=cartaescolhida-1
        terceira_anterior=cartaescolhida-3
        posicao_escolhida= peganumerodacarta("Duas possibilidades! {0} ou {1}?".format((anterior+1), (terceira_anterior+1)), mesa)
        while posicao_escolhida!=anterior and posicao_escolhida!=terceira_anterior:
            posicao_escolhida= peganumerodacarta("Inválido. Só duas possibilidades! {} ou {}?".format(anterior+1, terceira_anterior+1), mesa)
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

    
    if len(mesa) ==1:
        r= input ("Você ganhou, bora de novo?(s/n)")
        if r=='s':
            mesa= cria_baralho()
            pare=False
        else:
            print("Beleza! Talvez numa próxima!")
            pare=True
    elif possui_movimentos_possiveis(mesa)==0:
        r= input ("Você perdeu, aceita revanche?(s/n)")
        if r=='s':
            mesa= cria_baralho()
            pare=False
        else:
            print("Beleza! Talvez numa próxima!")
            pare=True

print(grifa("""
Bem, finalizamos por aqui. Se jogar não foi o suficiente, aqui vai uma curiosidade!:
Você sabia que uma das vertentes da origem do baralho diz que o jogo era a representação das classes sociais na França quando Carlos VI ainda era Rei?
Agora é trabalho teu descobrir qual naipe representava a burguesia, o clero, os militares e os camponeses! Fui :) 
"""))