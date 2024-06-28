import print_reprograma as pr

def imprimir_cabecalho():
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',sv=1,tamanho=100, margem=10,cor_texto='azul negrito',cor_barra='magenta')
    pr.separador(120,cor_texto='ciano')

def imprimir_rodape():
    pr.imprimir('[H] Ajuda ','[Q] Sair ',caracter='═',tamanho=115,alinhar='fim',end='╣')

    return input().lower()

def menu():
    opcao = ''
    while(opcao != 'q'):
        imprimir_cabecalho()
        opcao = imprimir_rodape()

menu()