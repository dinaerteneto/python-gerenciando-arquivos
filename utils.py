import os

def header():
    print("*************************************************")
    print("*************** CAIXA ELETRÔNICO ****************")
    print("*************************************************")


def pause() :
    input('Presione <ENTER> para continuar...') 


def clear() :
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)