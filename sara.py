import os
import sys

from lib.banner import banner
from lib.dorks import google
from lib.verify import personal
from lib.verify import domain
from lib.dorks import dorkfun
from lib.view import *
from lib.encrypt import *
from lib.network import *
from lib.distance import *



os.system("clear")

def help():
    banner()
    print("""
        \033[32m
        .sara [arg1] [arg2] ...
        python3 sara.py [arg1] [arg2] ...
        \033[m

        \033[34m
        -h --help - G
        \033[m

            \033[34m-s --search -\033[m        \033[32m-s --search domain @domain.com\033[m          \033[35m- Domínio\033[m
            \033[34m-s --search -\033[m        \033[32m-s --search personal user@user.com\033[m      \033[35m- Domínio\033[m
            \033[34m-p --pdf -\033[m           \033[32m-p --pdf      \033[m                          \033[35m-  Null\033[m
            \033[34m-e --encrypt -\033[m       \033[32m-e --encrypt                   \033[m         \033[35m-  Null\033[m
            \033[34m-d --decrypt -\033[m       \033[32m-d --decrypt                      \033[m      \033[35m-  Null\033[m
            \033[34m-n --network - \033[m      \033[32m-n --network\033[m                            \033[35m-  username\033[m
            \033[34m-v --view -  \033[m        \033[32m-v --view <navegador>\033[m                   \033[35m-  chorme - firefox\033[m
            \033[34m-m --distance <senha> <model> <porcentagem de retorno>\033[m       \033[35m- hamming - levenshtein - jaccard - sorensen\033[m


        """)




argumentos = sys.argv


if len(argumentos) < 2:
    print("Falta argumentos")
    exit()

if argumentos[1] == '-s' or argumentos[1] == '--search':
    banner()
    if len(argumentos) < 4:
        print("Falta argumentos")
        exit()
    if argumentos[2] == 'domain':
        try:
            result = dorkfun(argumentos[3])
            google(f"{argumentos[3]}")
            google(f"site: pastebin.com '{argumentos[3]}'")
            domain()
            for c in result:
                print(c)
        except:
            print("Muitas Tentativas, Tentando outra maneira.")
            try:
                google(f"{argumentos[3]}")
                google(f"site: pastebin.com '{argumentos[3]}'")

                domain()

            except:
                print("Tente novamente mais tarde.")

    elif argumentos[2] == 'personal':
        try:
            result = dorkfun(argumentos[3])
            google(f"{argumentos[3]}")
            google(f"site: pastebin.com '{argumentos[3]}'")
            with open("archives/vazamentos.txt", "r") as file:
                for line in file:
                    line = line.replace("\n", "")
                    personal(argumentos[3], line)
        except:
            print("Muitas Tentativas, Tentando outra maneira.")
            google(f"{argumentos[3]}")
            google(f"site: pastebin.com '{argumentos[3]}'")
            print("="*10)
            with open("archives/vazamentos.txt", "r") as file:
                for line in file:
                    line = line.replace("\n", "")
                    personal(line, argumentos[3])
    else:
        help()

elif argumentos[1] == '-p' or argumentos[1] == '--pdf':
    try:
        banner()
        pdf_gen()
    except:
        print("Erro")


elif argumentos[1] == '-e' or argumentos[1] == '--encrypt':
    banner()
    encryptfun()

elif argumentos[1] == '-d' or argumentos[1] == '--decrypt':
    banner()
    decryptfun()

elif argumentos[1] == '-n' or argumentos[1] == '--network':
    banner()
    if len(argumentos) < 2:
        print("Falta argumentos")
        exit()
    try:
        result = dorknet(argumentos[2])
        googlenet(f"{argumentos[2]}")
        googlenet(f"site: pastebin.com '{argumentos[2]}'")
        googlenet(f"intext:'t.me + {argumentos[2]}'")
        googlenet(f"inurl:'t.me + {argumentos[2]}'")
        googlenet(f"inurl:'twitter.com && intext:{argumentos[2]}'")
        googlenet(f"inurl:'facebook.com && intext:{argumentos[2]}'")
        with open("archives/vazamentos.txt", "r") as file:
            for line in file:
                line = line.replace("\n", "")
                personal(argumentos[2], line)

    except:
        print("Muitas Tentativas, Tentando outra maneira.")
        googlenet(f"{argumentos[2]}")
        googlenet(f"site: pastebin.com '{argumentos[2]}'")
        googlenet(f'tipo; inurl:"twitter.com" && intext:"{argumentos[2]}"')
        googlenet(f"intext:'t.me + {argumentos[2]}'")
        googlenet(f"inurl:'t.me + {argumentos[2]}'")
        print("="*10)
        with open("archives/vazamentos.txt", "r") as file:
            for line in file:
                line = line.replace("\n", "")
                personal(line, argumentos[2])

elif argumentos[1] == '-v' or argumentos[1] == '--view':
    banner()
    to_html()
    chorme()

elif argumentos[1] == '-m' or argumentos[1] == '--distance':
    banner()
    distancefun(model=argumentos[2], senha=argumentos[3], percent_arg=argumentos[4])

elif argumentos[1] == '-h' or argumentos[1] == '--help':
    help()

else:
    help()
