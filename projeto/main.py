import print_reprograma as pr
from datetime import datetime

compra_moc = [
    {'codigo':1,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 1','valor':10.00,'quantidade':1},
    {'codigo':2,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 2','valor':10.00,'quantidade':2},
    {'codigo':3,'nome':'Book - Web Programming Languages For Smart Students','valor':10.00,'quantidade':3}
]

def imprime_compra(compra):
    if(len(compra) > 0):
        total = 0
        pr.imprimir('codigo', tamanho=6, alinhar='centro',end='|')
        pr.imprimir('produto', tamanho=83, alinhar='centro',end='|')
        pr.imprimir('qtd', tamanho=3, alinhar='centro', end='|')
        pr.imprimir('valor un.', tamanho=12, alinhar='centro', end='|')
        pr.imprimir('valor', tamanho=12, alinhar='centro')   
        for produto in compra:
            total += produto['valor'] * produto['quantidade']
            imprimir_produto(produto)
        pr.separador(120,caracter='-')
        pr.imprimir('Subtotal', tamanho=107, alinhar='fim', end='|')
        pr.imprimir('R$',str(round(total, 2)), tamanho=12, alinhar='fim')
    else:
        pr.imprimir('Sem itens na lista ainda', tamanho=120, alinhar='center')
    pr.pular_linha()
    pr.pular_linha()

def imprimir_produto(produto):
    pr.imprimir(str(produto['codigo']), tamanho=6, alinhar='fim', caracter='0', end='|')
    pr.imprimir(produto['nome'], tamanho=83, caracter='.', end='|')
    pr.imprimir(str(produto['quantidade']), tamanho=3, caracter='0', alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'], 2)), tamanho=12, alinhar='fim', end='|')
    pr.imprimir('R$',str(round(produto['valor'] * produto['quantidade'], 2)), tamanho=12, alinhar='fim')    

def imprimir_cabecalho(erro):
    pr.limpar()
    pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',sv=1,tamanho=100, margem=10,cor_texto='azul negrito',cor_barra='magenta')
    pr.separador(120,cor_texto='ciano')
    if(erro != ''):
        pr.imprimir(erro,tamanho=120,alinhar='centro',cor_texto='vermelho negrito')
        pr.separador(120,cor_texto='ciano')
    erro = ''

def imprimir_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H]   >> Ajuda com o Sistema',alinhar='centro',tamanho=120)
    pr.imprimir('[Q]   >> Sair da Tela ou Sistema',alinhar='centro',tamanho=120)
    pr.imprimir('[N]   >> Cria uma Nova Compra',alinhar='centro',tamanho=120)
    pr.imprimir('[F]   >> Fechar a Compra',alinhar='centro',tamanho=120)
    pr.imprimir('[P]   >> Confirmar que a compra foi paga',alinhar='centro',tamanho=120)
    pr.imprimir('[nnn] >> Adicionar o codigo do produto a compra',alinhar='centro',tamanho=120)
    pr.imprimir('[Xnn] >> Muda a quantidade de itens adicionado',alinhar='centro',tamanho=120)
    pr.imprimir('[E]   >> Encerar caixa',alinhar='centro',tamanho=120)
    pr.pular_linha(quantidade=2)

def imprimir_rodape():
    pr.imprimir('[H] Ajuda ','[Q] Sair ',caracter='═',tamanho=115,alinhar='fim',end='╣')

    return input().lower()

def menu():
    opcao = ''
    erro = ''
    tela = ''
    compra = compra_moc
    while(opcao != 'q'):
        imprimir_cabecalho(erro)
        if(tela == ''):
            pr.pular_linha(quantidade=4)
        elif(tela == 'ajuda'):
            imprimir_ajuda()
            tela=''
        elif(tela == 'compra'):
            imprime_compra(compra)    
        opcao = imprimir_rodape()
        if(opcao == 'h'):
            tela='ajuda'
        elif(opcao == 'n'):
            tela='compra'
        else:
            erro = 'A opção selecionada não existe no sistema'

menu()


