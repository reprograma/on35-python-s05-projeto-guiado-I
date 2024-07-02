import print_reprograma as pr
from datetime import datetime

produtos = [
    {'codigo':1,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 1','valor':10.00},
    {'codigo':2,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 2','valor':10.00},
    {'codigo':3,'nome':'Book - Web Programming Languages For Smart Students','valor':10.00},
    {'codigo':4,'nome':'Book - Scripting Technologies For Smart Students','valor':10.00},
    {'codigo':5,'nome':'Book - Web Development Using Sql For Smart Students','valor':15.00},
    {'codigo':6,'nome':'Book - Web Development Using C++ For Smart Students','valor':15.00},
    {'codigo':7,'nome':'Book - Web Development Using Java For Smart Students','valor':15.00},
    {'codigo':8,'nome':'Web Development Using .Net For Smart Students','valor':15.00},
    {'codigo':9,'nome':'Book - Pc Hardware & Networking For Smart Students - Volume 1','valor':15.00},
    {'codigo':10,'nome':'Book - Pc Hardware & Networking For Smart Students - Volume 2','valor':15.00},
    {'codigo':11,'nome':'Book - Pc Hardware & Networking For Smart Students - Volume 3','valor':15.00},
    {'codigo':12,'nome':'Book - Pc Hardware & Networking For Smart Students - Volume 4','valor':15.00},
    {'codigo':13,'nome':'Book - Mastering English For Smart Students','valor':5.00},
    {'codigo':14,'nome':'Book - Business Communication For Smart Students','valor':10.00},
    {'codigo':15,'nome':'Business Communication Dvd','valor':2.00},
    {'codigo':16,'nome':'Personality Development Dvd','valor':4.00},
    {'codigo':17,'nome':'Set Of 2 Dvd9 Self Learning Cbts (Hindi)','valor':5.00},
    {'codigo':18,'nome':'Book - Personality Development For Smart Students - Book 1','valor':15.00},
    {'codigo':19,'nome':'Book - Personality Development For Smart Students - Book 2','valor':15.00},
    {'codigo':20,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 1','valor':10.00},
    {'codigo':21,'nome':'Book - Computer Fundamentals & Office Tools For Smart Students - Volume 2','valor':10.00},
    {'codigo':22,'nome':'NOURISH Noni Gold -1ltr','valor':10.00},
    {'codigo':23,'nome':'NOURISH Noni Gold 500ml','valor':5.00},
    {'codigo':24,'nome':'NOURISH Noni Kokum Plus 500ml','valor':5.00},
    {'codigo':25,'nome':'NOURISH Noni Kokum Plus 1000ml','valor':10.00},
    {'codigo':26,'nome':'NOURISH Noni Premium Plus 500ml','valor':6.00},
    {'codigo':27,'nome':'NOURISH Noni Premium Plus 1000ml','valor':12.00},
    {'codigo':28,'nome':'NOURISH Protein Powder 200gm','valor':5.00},
    {'codigo':29,'nome':'NOURISH Protein Powder 500gm','valor':10.00},
    {'codigo':30,'nome':'NOURISH Energy Rush - Chocolate 200gm','valor':1.00},
    {'codigo':31,'nome':'NOURISH Energy Rush - Butter Scotch 200gm','valor':1.00},
    {'codigo':32,'nome':'NOURISH Protein Rich - Chocolate 200gm','valor':3.00},
    {'codigo':33,'nome':'NOURISH Protein Rich - Butter Scotch 200gm','valor':3.00},
    {'codigo':34,'nome':'NOURISH Aloe Vera Juice 500ml','valor':1.00},
    {'codigo':35,'nome':'NOURISH Amla Juice 500ml','valor':0.70},
    {'codigo':36,'nome':'NATURALS Amla Sweet Candy 500gm','valor':0.50},
    {'codigo':37,'nome':'NATURALS Amla Chatpata Candy 500gm','valor':0.50},
    {'codigo':38,'nome':'NOURISH Antioxidants Coenzyme Q10 Men – 30 Capsules','valor':2.50},
    {'codigo':39,'nome':'NOURISH Antioxidants Coenzyme Q10 Women – 30 Capsules','valor':2.00},
    {'codigo':40,'nome':'NOURISH Iron and Folic Acid – 30 Capsules','valor':2.50},
    {'codigo':41,'nome':'NOURISH Omega 3 Fatty Acid – 30 Capsules','valor':2.50},
    {'codigo':42,'nome':'NOURISH Green Coffee Extracts – 30 Capsules','valor':2.00},
    {'codigo':43,'nome':'NOURISH Joint Care – 30 Capsules','valor':2.50},
    {'codigo':44,'nome':'NOURISH Spirulina – 90 Capsules','valor':5.00},
    {'codigo':45,'nome':'NOURISH Calcium – 100 Tablets','valor':3.00},
    {'codigo':46,'nome':'NOURISH Multi Vitamins & Minerals – 90 Capsules','valor':5.00},
    {'codigo':47,'nome':'NOURISH Pain Oil 100ml','valor':0.50},
    {'codigo':48,'nome':'NURTURE Green Apple Shampoo With Aloe Vera 200ml','valor':0.50},
    {'codigo':49,'nome':'NURTURE Anti Dandruff Shampoo 200ml','valor':0.50},
    {'codigo':50,'nome':'NURTURE Boosting Conditioner 200ml','valor':0.50},
    {'codigo':51,'nome':'NURTURE Herbal Hair Tonic Oil 100ml','valor':0.25},
    {'codigo':52,'nome':'NURTURE Mahabhrinraj Jadi Booti Hair Oil 100ml','valor':0.50},
    {'codigo':53,'nome':'NURTURE Pure Cocnut Oil','valor':0.10},
    {'codigo':54,'nome':'NURTURE Moisturising Lotion With SPF 15 - 100ml','valor':0.20},
    {'codigo':55,'nome':'NURTURE Wheat Germ Moisturising Lotion 100ml','valor':0.20},
    {'codigo':56,'nome':'Vivita Soap - Set Of 5','valor':0.60},
    {'codigo':57,'nome':'NURTURE Ayurvedic Gel Toothpaste 100gm','valor':0.20},
    {'codigo':58,'nome':'NURTURE Hand Wash 250ml','valor':0.25},
    {'codigo':59,'nome':'NURTURE Aloe Vera And Lemon Anti Bacterial Hand Wash- 200ml','valor':0.25},
    {'codigo':60,'nome':'NURTURE Fairness Cream 100gm','valor':0.40},
    {'codigo':61,'nome':'NURTURE Strawberry Lip Balm 10gm','valor':0.20},
    {'codigo':62,'nome':'NURTURE Neem And Aloevera Face Wash 100ml','valor':0.40},
    {'codigo':63,'nome':'NURTURE Apricot Almond Scrub 100gm','valor':0.40},
    {'codigo':64,'nome':'Smart Shave - Shaving Brush','valor':0.12},
    {'codigo':65,'nome':'SmartValue Shaving Razor','valor':0.06},
    {'codigo':66,'nome':'NURTURE Noni Based Products Kit - 1','valor':30.00},
    {'codigo':67,'nome':'NURTURE Noni Based Products Kit - 2','valor':50.00},
    {'codigo':68,'nome':'Smart Shine Dishwash Bar 200gm (Set Of 4)','valor':0.22},
    {'codigo':69,'nome':'Smart Wash Detergent Bar 200gm (Set Of 4)','valor':0.22},
    {'codigo':70,'nome':'Smart Wash Detergent Powder 700gm','valor':0.30},
    {'codigo':71,'nome':'SmartValue Travel Bag','valor':2.00},
    {'codigo':72,'nome':'Fabric Combo 1 - Shirt Plus Pant','valor':18.30},
    {'codigo':73,'nome':'Fabric Combo 2 - Shirt Plus Pant','valor':18.30},
    {'codigo':74,'nome':'Fabric Combo 3 - Shirt Plus Pant','valor':18.30},
    {'codigo':75,'nome':'Suit Length 3mtr','valor':35.00},
    {'codigo':76,'nome':'Handkerchiefs - Pack Of 3','valor':1.00},
    {'codigo':77,'nome':'Socks - Pack Of 3','valor':2.00},
    {'codigo':78,'nome':'SV Woven Polyster Tie','valor':0.80},
    {'codigo':79,'nome':'Woven Polyester Tie - Assorted','valor':0.80},
    {'codigo':80,'nome':'Saathi Pair Of Watches (Gold Plated)','valor':20.00},
    {'codigo':81,'nome':'Black Plated Ladies Wrist Watch','valor':4.00},
    {'codigo':82,'nome':'Brown Strap Gold And Silver Plated Men','valor':3.00},
    {'codigo':83,'nome':'SmartValue SMARTea 250gm','valor':0.11},
    {'codigo':84,'nome':'Agrolizer 82 500ml','valor':5.00}
]

def produto_codigo(codigo):
    for produto in produtos:
        if(produto['codigo'] == codigo):
            return produto

def imprimir_cabecalho(erro_para_imprimir):
   pr.limpar()
   pr.retangulo('{reprograma}\n Projeto Guiado I\n Terminal de Vendas', tamanho=120, cor_barra='magenta', cor_texto='amarelo')
   pr.separador(120, cor_texto='magenta')

   if(erro_para_imprimir != ''):
    pr.imprimir(erro_para_imprimir, cor_texto='vermelho negrito', tamanho=120, alinhar='centro')
    pr.separador(120, cor_texto='magenta')

def imprimir_rodape():
   pr.imprimir('[S] Sair', '[H] Ajuda', tamanho=110, alinhar='fim', caracter='═', end='┤')
   return input().lower()

def imprimir_tela_inicial():
    pr.pular_linha(quantidade=2)
    pr.imprimir('Tela inicial',tamanho=120,alinhar='centro')
    pr.pular_linha(quantidade=2)

def imprimir_tela_ajuda():
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H] - Abre a tela de ajuda com todos os comandos', tamanho=120)
    pr.imprimir('[S] - Fecha o sistema inteiro',tamanho=120)
    pr.imprimir('[N] - Abre uma nova compra')
    pr.imprimir('[nn] - Adiciona o código nn que foi passado na compra')
    pr.imprimir('[F] - Fechar a compra que está em aberto')
    pr.imprimir('[P] - Compra foi paga')
    pr.imprimir('[E] - Encerrar o caixa do dia')
    pr.imprimir('[X00]  - Muda a quantidade para o valor 00 informado')
    pr.pular_linha(quantidade=2)

def imprimir_compra_fechada(compra, valor_total, descontos):
    pr.imprimir('codigo',tamanho=6,end='│',alinhar='centro')
    pr.imprimir('produto',tamanho=83,end='│',alinhar='centro')
    pr.imprimir('qnt',tamanho=3,end='│',alinhar='centro')
    pr.imprimir('valor un.',tamanho=12,end='│',alinhar='centro')
    pr.imprimir('valor',tamanho=12,alinhar='centro')
    pr.separador(120,caracter='─')

    total = 0

    for item in compra:

        pr.imprimir(str(item['codigo']),tamanho=6,end='│',alinhar='fim',caracter='0')
        pr.imprimir(item['nome'],tamanho=83,end='│',caracter='.')
        pr.imprimir(str(item['quantidade']),tamanho=3,end='│',alinhar='fim')
        pr.imprimir('R$',str(round(item['valor'],2)),tamanho=12,end='│',alinhar='fim')
        pr.imprimir('R$',str(round(item['valor'] * item['quantidade'],2)),tamanho=12,alinhar='fim')

        total += item['valor'] * item['quantidade']
    pr.separador(120,caracter='─')

    pr.imprimir('Total',tamanho=107,end='│',alinhar='fim')
    pr.imprimir('R$',str(round(total,2)),tamanho=12,alinhar='fim')

    for desconto in descontos:
        pr.imprimir(desconto['descricao'],tamanho=107,end='│',alinhar='fim')
        pr.imprimir('-R$',str(round(desconto['valor'],2)),tamanho=12,alinhar='fim',cor_texto='vermelho negrito')
    pr.imprimir('Total a pagar',tamanho=107,end='│',alinhar='fim')
    pr.imprimir('R$',str(round(valor_total,2)),tamanho=12,alinhar='fim',cor_texto='verde negrito')


def imprimir_nova_compra(compra,quantidade):

    if(len(compra) > 0 ):

        pr.imprimir('codigo',tamanho=6,end='│',alinhar='centro')
        pr.imprimir('produto',tamanho=83,end='│',alinhar='centro')
        pr.imprimir('qnt',tamanho=3,end='│',alinhar='centro')
        pr.imprimir('valor un.',tamanho=12,end='│',alinhar='centro')
        pr.imprimir('valor',tamanho=12,alinhar='centro')
        pr.separador(120,caracter='─')

        subtotal = 0

        for item in compra:

            pr.imprimir(str(item['codigo']),tamanho=6,end='│',alinhar='fim',caracter='0')
            pr.imprimir(item['nome'],tamanho=83,end='│',caracter='.')
            pr.imprimir(str(item['quantidade']),tamanho=3,end='│',alinhar='fim')
            pr.imprimir('R$',str(round(item['valor'],2)),tamanho=12,end='│',alinhar='fim')
            pr.imprimir('R$',str(round(item['valor'] * item['quantidade'],2)),tamanho=12,alinhar='fim')

            subtotal += item['valor'] * item['quantidade']
        if(quantidade > 1):
            pr.imprimir('x',str(quantidade),alinhar='fim',tamanho=120)
        pr.separador(120,caracter='─')

        pr.imprimir('Subtotal',tamanho=107,end='│',alinhar='fim')
        pr.imprimir('R$',str(round(subtotal,2)),tamanho=12,alinhar='fim')
    else:
        pr.pular_linha(quantidade=2)
        pr.imprimir('Essa compra não tem itens ainda',tamanho=120,alinhar='centro')
        pr.pular_linha(quantidade=2)


def imprimir_caixa_encerrada(compras):

    pr.imprimir('Data',tamanho=92,end='│',alinhar='centro')
    pr.imprimir('Itens',tamanho=6,end='│',alinhar='centro')
    pr.imprimir('Valor',tamanho=20,alinhar='centro')
    pr.separador(120,caracter='─')

    total = 0

    for compra in compras:
        pr.imprimir(compra['data'].strftime("%d/%m/%Y %H:%M:%S"),tamanho=92,end='│',alinhar='fim')
        pr.imprimir(str(len(compra['compra'])),tamanho=6,end='│',alinhar='centro')
        pr.imprimir('R$',str(round(compra['valor'],2)),tamanho=20,alinhar='fim')

        total += compra['valor']
    pr.separador(120,caracter='─')

    pr.imprimir('Total de vendas do caixa',tamanho=107,end='│',alinhar='fim')
    pr.imprimir('R$',str(round(total,2)),tamanho=12,alinhar='fim',cor_texto='vermelho negrito')

def valor_total_pagar(compra):

    descontos = []
    total = 0

    quantidade_codigo_10 = 0

    for item in compra:

        if(item['codigo']==10):
            quantidade_codigo_10 += item['quantidade']
        total = total + (item['valor'] * item['quantidade'])

    if(quantidade_codigo_10 >= 2):
        produto_10 = produto_codigo(10)
        total = total - produto_10['valor'] * (1 - 0.5)
        descontos.append({'descricao':'50% no segundo produto ' + produto_10['nome'],'valor':(produto_10['valor'] * 0.5)})

    if(total > 100):
        descontos.append({'descricao':'10% de desconto na compra acima de R$ 100,00','valor':(total * 0.1)})
        total = total * (1 - 0.10)

    return {'valor':total, 'descontos':descontos}


opcao = ''
erro = ''
tela = ''
compra = []
compras = []
total_compra = 0
descontos_compra = []
quantidade = 1

while(True):
    imprimir_cabecalho(erro)
    erro = ''

    if(tela == ''):
        imprimir_tela_inicial()
    elif(tela == 'ajuda'):
        imprimir_tela_ajuda()
        tela=''
    elif(tela == 'nova'):
        imprimir_nova_compra(compra,quantidade)
    elif(tela == 'fechada'):
        imprimir_compra_fechada(compra,total_compra,descontos_compra)
    elif(tela == 'encerrar'):
        imprimir_caixa_encerrada(compras)

    opcao = imprimir_rodape()

    if(opcao == 's'):
        break
    elif(opcao == 'h'):
        tela = 'ajuda'
    elif(opcao == 'n'):
        tela = 'nova'
    elif(opcao == 'f'):
        tela = 'fechada'
        total_calculado = valor_total_pagar(compra)
        total_compra = total_calculado['valor']
        descontos_compra = total_calculado['descontos']
    elif(opcao == 'p'):
        compras.append({
            'compra': compra,
            'valor': total_compra,
            'data': datetime.now()
        })

        compra = []

        tela = ''
    elif(opcao == 'e'):
        tela = 'encerrar'
    elif('x' in opcao):
        quantidade = int(opcao.replace('x',''))
    else:
        try:
            codigo_produto = int(opcao)
            produto = produto_codigo(codigo_produto)
            compra.append({
                'codigo':produto['codigo'],
                'nome':produto['nome'],
                'valor':produto['valor'],
                'quantidade':quantidade
            })
            quantidade = 1
        except:
            erro = 'A opção não existe!!!'
        