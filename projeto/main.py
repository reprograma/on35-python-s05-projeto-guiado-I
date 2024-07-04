import print_reprograma as pr
def imprimir_ajuda():
    pr.imprimir('Ajuda')


opcao = ''
erro = ''
tela = ''
while ((opcao != 's') and (opcao != 'sair')):
    pr.limpar
    pr.retangulo('{Reprograma}\n Projeto Guiado I\nTerminal de vendas', tamanho=120, cor_barra='magenta',cor_texto='azul')
    pr.separador(120, cor_texto= 'azul')
    #erro 
    if(erro != ''):
        pr.imprimir(erro,cor_texto='vermelho negrito', tamanho=120, alinhar='centro')
        pr.separador(120,cor_texto='azul')

        #tela ajuda 
    if (tela == ''):
        pr.imprimir('tela inicial')
    
    pr.imprimir('[S]Sair', '[H]Ajuda',tamanho=120,alinhar='fim', caracter= '═', end='┤')

    #o end pula uma linha. 

    opcao = input().lower()
    if((opcao != 's') or (opcao != 'sair')):
        break
    elif (opcao == 'h'):
        tela = 'ajuda'
    else: 
        erro = 'A opçaõ não existe!!!'
