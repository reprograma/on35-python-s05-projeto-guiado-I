def get_cor():
    print(cor_texto)

def branco():
    cor_texto = 'branco'
    print('\033[30m', end='')
 
def vermelho():
    cor_texto = 'vermelho'
    print('\033[31m', end='')
 
def verde():
    cor_texto = 'verde'
    print('\033[32m', end='')
 
def amarelo():
    cor_texto = 'amarelo'
    print('\033[33m', end='')
 
def azul():
    cor_texto = 'azul'
    print('\033[34m', end='')

def magenta():
    cor_texto = 'magenta'
    print('\033[35m', end='')

def ciano():
    cor_texto = 'ciano'
    print('\033[36m', end='')

def cinza():
    cor_texto = 'cinza'
    print('\033[37m', end='')

def negrito():
    print('\033[1m', end='')

def branco_negrito():
    print('\033[1;30m', end='')
 
def vermelho_negrito():
    print('\033[1;31m', end='')
 
def verde_negrito():
    print('\033[1;32m', end='')
 
def amarelo_negrito():
    print('\033[1;33m', end='')
 
def azul_negrito():
    print('\033[1;34m', end='')

def magenta_negrito():
    print('\033[1;35m', end='')

def ciano_negrito():
    print('\033[1;36m', end='')

def cinza_negrito():
    print('\033[1;37m', end='')

def cor(cor):
    if(cor == 'branco'):
        branco()
    elif(cor == 'vermelho'):
        vermelho()
    elif(cor == 'verde'):
        verde()
    elif(cor == 'amarelo'):
        amarelo()
    elif(cor == 'azul'):
        azul()
    elif(cor == 'magenta'):
        magenta()
    elif(cor == 'ciano'):
        ciano()
    elif(cor == 'cinza'):
        cinza()
    elif(cor == 'w'):
        branco()
    elif(cor == 'r'):
        vermelho()
    elif(cor == 'g'):
        verde()
    elif(cor == 'y'):
        amarelo()
    elif(cor == 'b'):
        azul()
    elif(cor == 'm'):
        magenta()
    elif(cor == 'c'):
        ciano()
    elif(cor == 'gr'):
        cinza()
    elif(cor == 'branco negrito'):
        branco_negrito()
    elif(cor == 'vermelho negrito'):
        vermelho_negrito()
    elif(cor == 'verde negrito'):
        verde_negrito()
    elif(cor == 'amarelo negrito'):
        amarelo_negrito()
    elif(cor == 'azul negrito'):
        azul_negrito()
    elif(cor == 'magenta negrito'):
        magenta_negrito()
    elif(cor == 'ciano negrito'):
        ciano_negrito()
    elif(cor == 'cinza negrito'):
        cinza_negrito()
    elif(cor == 'wb'):
        branco_negrito()
    elif(cor == 'rb'):
        vermelho_negrito()
    elif(cor == 'gb'):
        verde_negrito()
    elif(cor == 'yb'):
        amarelo_negrito()
    elif(cor == 'bb'):
        azul_negrito()
    elif(cor == 'mb'):
        magenta_negrito()
    elif(cor == 'cb'):
        ciano_negrito()
    elif(cor == 'grb'):
        cinza_negrito()
    elif(cor == 'negrito'):
        negrito()

def imprimir(*textos, sep=' ',end='\n', caracter = ' ', tamanho=0, alinhar='comeco', cor_texto=''):
    cor(cor_texto)
    tamanho_total = 0
    for texto in textos:
        tamanho_total += len(texto)
    tamanho_total += (len(textos)-1) * len(sep)
    
    espaco_ini = 0
    espaco_fim = 0

    if(alinhar == 'fim'):
        espaco_ini = tamanho - tamanho_total
        espaco_fim = 0
    elif(alinhar == 'centro'):
        espaco_ini = (tamanho - tamanho_total)//2
        espaco_fim = (tamanho - tamanho_total)//2
        if((tamanho - tamanho_total) % 2 > 0):
            espaco_fim += 1
    else:
        espaco_ini = 0
        espaco_fim = tamanho - tamanho_total

    if(espaco_ini < 0):
        espaco_ini = 0

    if(espaco_fim < 0):
        espaco_fim = 0

    for i in range(espaco_ini):
        print(caracter, end='')

    for i in range(len(textos)):
        temp_sep = sep
        if(i == len(textos) - 1):
            temp_sep = ''
        else:
            tamanho_total += 1
        print(textos[i], end = temp_sep)
    
    for i in range(espaco_fim):
        print(caracter, end='')

    print(end, end='')

    limpar_formatacao()

def separador(tamanho,caracter = '═', cor_texto=''):
    cor(cor_texto)
    for i in range(tamanho):
        print(caracter,end='')
    print('\n')
    limpar_formatacao()

def retangulo(texto,sv=0,sh=0,tamanho=0,cor_barra = '', cor_texto = '',margem=0):
    linhas = texto.split('\n')
    max_len = 0
    for linha in linhas:
        if(max_len < len(linha)):
            max_len = len(linha)
    ajuste = False
    if(tamanho>0):
        sh = (tamanho - max_len - 2) // 2
        if(sh < 0):
            sh = 0
        else:
            ajuste = (tamanho - max_len - 2) % 2 > 0
    cor(cor_barra)
    sh_texto_ini = ''
    sh_barra_ini = ''
    sh_texto_fim = ''
    sh_barra_fim = ''
    for i in range(sh):
        sh_texto_ini += ' '
        sh_barra_ini += '═'
        sh_texto_fim += ' '
        sh_barra_fim += '═'
    if(ajuste):
        sh_texto_fim += ' '
        sh_barra_fim += '═'
    texto_branco = ''
    texto_barra = ''
    margem_texto = ''
    for i in range(margem):
        margem_texto += ' '
    for i in range(max_len):
        texto_barra+= '═' 
        texto_branco += ' '
    print(margem_texto,'╔',sh_barra_ini,texto_barra,sh_barra_fim,'╗',sep='')
    for i in range(sv):
        print(margem_texto,'║',sh_texto_ini,texto_branco,sh_texto_fim,'║',sep='')
    
    for linha in linhas:
        cor(cor_barra)
        print(margem_texto,'║',end='',sep='')
        cor(cor_texto)
        for i in range((max_len - len(linha))//2):
            print(' ',end='')
        print(sh_texto_ini,linha,sh_texto_fim,sep='',end='')
        for i in range((max_len - len(linha))//2):
            print(' ',end='')
        if((max_len - len(linha))%2 > 0):
            print(' ',end='')
        cor(cor_barra)
        print('║')

    for i in range(sv):
        print(margem_texto,'║',sh_texto_ini,texto_branco,sh_texto_fim,'║',sep='')

    print(margem_texto,'╚',sh_barra_ini,texto_barra,sh_barra_fim,'╝',sep='')
    limpar_formatacao()

def pular_linha(quantidade = 1):
    for i in range(quantidade):
        print('')

def limpar():
    print(chr(27) + "[2J")

def limpar_formatacao():
    print('\033[m', end='')