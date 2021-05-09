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
            cor_corrente = Fore.YELLOW
        #Três aspas== Conseguir escrever em multilinhas
        print(
            """
            
        {0}{1}.{2}
                  ┌─────────┐
                  │{3}░░░░░░░│
                  │░░░░░░░░░│
                  │░░░░░░░░░│
                  │░░░{4}░░░░░│
                  │░░░░░░░░░│
                  │░░░░░░░░░│
                  │░░░░░░░{3}│
                  └─────────┘""".format((Fore.WHITE),(i+1),(cor_corrente),(extrai_valor(mesa[i])),(extrai_naipe(mesa[i]))))
    print(Fore.WHITE)
    return