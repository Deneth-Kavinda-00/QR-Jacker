from colorama import Style,Fore
from banner import rand_choice

def color():
    num = rand_choice()
    if num == 1:
        return Fore.RED
    elif num == 2:
        return Fore.GREEN
    elif num == 3:
        return Fore.MAGENTA
    elif num == 4:
        return Fore.CYAN
    else:
        return Fore.YELLOW

def clear():
    return Style.RESET_ALL

def red():
    return Fore.RED

def blue():
    return Fore.BLUE