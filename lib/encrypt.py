import os

def encryptfun():
    os.system("ccencrypt archives/contents/emails.txt")
    print("Arquivo salvo em archives/contents/emails.txt.cpt")


def decryptfun():
    os.system("ccdecrypt archives/contents/emails.txt.cpt")
    print("Arquivo salvo em archives/contents/emails.txt")



