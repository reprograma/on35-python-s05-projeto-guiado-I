import print_reprograma as pr

opcao = ''
while(opcao != 's' and opcao != 'sair'):
  pr.limpar() 
  pr.imprimir('{Reprograma}\nProjeto Guiado I\nTerminal de Vendas',tamanho=120)
  pr.separador(120,cor_texto='azul')

  pr.imprimir('[S] Sair',tamanho=110,alinhar='fim',caracter='-', end='-|')

  opcao = input().lower()