from colorama import Fore, Back, Style
from funcoes import *
def print_estilizado(mesa):
    cor_corrente = Fore.WHITE
    
    for i in range (0, len(mesa)):
        naipe_corrente = extrai_naipe(mesa[i])
        if naipe_corrente == '♠':
            cor_corrente = Fore.BLUE
        
        elif naipe_corrente == '♣':
            cor_corrente= Fore.GREEN

        elif naipe_corrente == '♥':
            cor_corrente = Fore.RED
        
        else:
            cor_corrente = Fore.MAGENTA
        #Três aspas== Conseguir escrever em multilinhas
        #ljust(quantascasas)= Imprimir certa quantidade de casas e preencher com espaços se faltar (à direita)
        print(
"""
{0}{1}.{2}
{5}┌──────┐{6}
{5}│{3}░░░░│{6}
{5}│░░{4}░░░│{6}
{5}│░░░░{3}│{6}
{5}└──────┘{6}
"""
        .format(
            (Fore.WHITE),
            (i+1),
            (cor_corrente),
            (extrai_valor(mesa[i]).ljust(2)),
            (extrai_naipe(mesa[i])),
            (Back.WHITE),
            (Back.BLACK)
            )
        ,end="")  #end== Todo print tem como açao final uma quebra de linha (\n- "new line"), mas agora, definindo o end, eu pude tirar uma quebra de linha=== Cartas mais próximas!
    print(Fore.WHITE)
    return

def grifa(texto):
    return(Back.YELLOW+Fore.BLACK+texto+Fore.WHITE+Back.BLACK)