from colorama import *
import subprocess as sp
sp.call('clear', shell=True)

def icon():
    print(Fore.WHITE + """
   _____
    | |
    | |
   -----
    | |   SOLVER INJECTOR
    |""" + Fore.GREEN + "S" + Fore.WHITE + """|   
    |""" + Fore.GREEN + "O" + Fore.WHITE + """|   -PC injection toolkit 
    |""" + Fore.GREEN + "L" + Fore.WHITE + """|   -made for termux 
    |""" + Fore.GREEN + "V" + Fore.WHITE + """|   -requires data cable
    |""" + Fore.GREEN + "E" + Fore.WHITE + """|   -software made by Karkichan
    |""" + Fore.GREEN + "R" + Fore.WHITE + """|
    | |
     V
     |
    """)

def menu():
    print("[" + Fore.GREEN + "payloads" + Fore.WHITE + "]")
    print("")
    print(Fore.WHITE + "[" + Fore.GREEN + "1" + Fore.WHITE + "]" + Fore.GREEN + " slack Trojan")
    print(Fore.WHITE + "[" + Fore.GREEN + "2" + Fore.WHITE + "]" + Fore.GREEN + " XMR miner")
    print("")
    opt = input(Fore.WHITE +"[" + Fore.GREEN + "+" + Fore.WHITE + "] solver> ")




icon()
menu()
