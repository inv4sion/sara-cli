import pandas as pd
import numpy as np
import textdistance
import sys
import re


def distancefun(senha, model, percent_arg):
    df = pd.read_csv('archives/senhas.csv')

    high = {}
    mean = []

    def test(senha, model, percent_arg):
        if model == 'hamming' or model == 'ham':
            for password in df['Senhas']:
                percent = textdistance.hamming.normalized_similarity(f'{senha}', str(password))*100
                if percent >= int(percent_arg):
                    high[f'{password}'] = [senha, percent]
                    mean.append(percent)
                else:
                    pass
        elif model == 'levenshtein' or model == 'leven':
            for password in df['Senhas']:
                percent = textdistance.levenshtein.normalized_similarity(f'{senha}', str(password))*100
                if percent >= int(percent_arg):
                    high[f'{password}'] = [senha, percent]
                    mean.append(percent)
                else:
                    pass

        elif model == 'jaccard' or model == 'jac':
            for password in df['Senhas']:
                percent = textdistance.jaccard(f'{senha}', str(password))*100
                if percent >= int(percent_arg):
                    high[f'{password}'] = [senha, percent]
                    mean.append(percent)
                else:
                    pass
        elif model == 'sorensen' or model == 'soren':
            for password in df['Senhas']:
                percent = textdistance.sorensen(f'{senha}', str(password))*100
                if percent >= int(percent_arg):
                    high[f'{password}'] = [senha, percent]
                    mean.append(percent)
                else:
                    pass
        else:
            print("NaN")



    def password_len(senha):
        length = len(senha)
        return 1.7 * (10**-6) * (length**15) / 86400






    try:
        percent_arg =  int(percent_arg)
    except:
        print("\033[31mFalta um número\033[m")


    test(senha, model, percent_arg)
    for key,word in zip(high.keys(), high.items()):
        print('\033[32m{}\033[m - \033[33m{}\033[m - \033[33m{:.2f}\033[m' .format(key, word[1][0], word[1][1]))


    count = 0
    for c in mean:
        count += c
    try:
        print('='*8**2)
        print('\033[32mPorcentagem Geral: \033[m\033[34m{:.2f}\033[m' .format(count/len(mean)))
        print('='*8**2)
    except:
        print('='*8**2)
        print("\033[31mNão encontrado\033[m")
        print('='*8**2)

    print('='*8**2)
    print('\033[32m{:.2f}\033[m horas para quebrar essa senha' .format(password_len(f'{senha}')))
    print('='*8**2)


