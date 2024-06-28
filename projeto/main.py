import print_reprograma as pr

pr.limpar()
pr.retangulo('{reprograma}\nProjeto Guiado 1\nTerminal de Vendas',sv=1,tamanho=100, margem=10,cor_texto='azul negrito',cor_barra='magenta')
pr.separador(120,cor_texto='ciano')

pr.imprimir('[H] Ajuda ','[Q] Sair ',caracter='═',tamanho=115,alinhar='fim',end='╣')

opcao = input().lower()

pr.imprimir(opcao)