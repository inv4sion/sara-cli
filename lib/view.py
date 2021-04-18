import pdfkit
import time
import os






def pdf_gen():
    with open("view/index.html", "w") as arquivo:
        arquivo.write('<style>html{text-aling:center;}</style>')
        arquivo.write('<center><h1>Emails Achados</h1></center>')
        arquivo.write("<br><br>")
        with open("archives/contents/emails.txt", "r") as emails_file:
            for linha in emails_file:
                arquivo.write(f"<center><h3>{linha}</h3></center>")

    print("\033[32mIsso pode levar alguns segundos\033[m")
    pdfkit.from_url('view/index.html', 'data/emails.pdf')
    print("\033[32mPDF Gerado\033[m")




def chrome():
    pdf_gen()
    os.system("google-chrome view/index.html")


