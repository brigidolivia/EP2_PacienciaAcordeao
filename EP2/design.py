from colorama import Fore, Back, Style
from funcoes import *
def print_estilizado(mesa):
    cor_corrente = Fore.WHITE
    
    for i in range (0, len(mesa)):
        naipe_corrente = extrai_naipe(mesa[i])
        if naipe_corrente == '♠' or naipe_corrente == '♣':
            cor_corrente = Fore.BLUE
        elif naipe_corrente == '♥' or naipe_corrente == '♦':
            cor_corrente = Fore.RED
        print(cor_corrente+
        """
        {0}. 
        {1}
        """
        .format((i+1),(mesa[i])))
    print(Fore.WHITE)
    return