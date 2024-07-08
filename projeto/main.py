import print_reprograma as pr

# pr.imprimir('Olá mundo', tamanho=120, alinhar="meio",cor_texto="amarelo")

# pr.retangulo('Olá mundo')

def imprimir_ajuda():
    pr.imprimir('Ajuda')

opcao = ''
erro = ' '
tela = ' '

while((opcao != 's') and (opcao != 'sair')):
    pr.limpar() #Comando para limpar o terminal sempre
    pr.retangulo('{reprograma}\nProjeto Guiado I\nTerminal de Vendas',tamanho=100,cor_barra='magenta',cor_texto='azul')
    pr.separador(100,cor_texto='azul')

    if(erro != ' '):
        pr.imprimir(erro, cor_texto='vermelho negrito', tamanho=100,alinhar='centro')
        pr.separador(100,cor_texto='azul')

    if(tela == ' '):
        pr.imprimir('tela inicial')
    elif(tela == 'Ajuda'):
        imprimir_ajuda()
    
    #Tela de ajuda

    pr.imprimir('[S] Sair', '[H] Ajuda' tamanho=90, alinhar='fim', caracter='═',end='┤')
    opcao = input().lower() #o lower é usado para entender a saida mesmo colocando maiusculo ou menusculo
    if(opcao == 'h'):
    
    else:
        erro = 'A opção não existe!!'
        