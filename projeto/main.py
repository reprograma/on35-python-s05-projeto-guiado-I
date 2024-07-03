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
        
#preparando a função que imprimi o cabeçalho e a mensagem de erro
def imprimir_cabecalho(erro_para_imprimir):
    #limpa a tela(igual dar um clear no terminal)
    pr.limpar()
    #mostra o texo inicial
    pr.retangulo("{Reprograma}\nProjeto Guiado I\n Terminal de vendas",tamanho=120,cor_barra="magenta",cor_texto="azul")
    pr.separador(120,cor_texto="azul")
    #se tiver uma mensagem de erro para exibir eu mostro, se não eu não faço nada
    if(erro_para_imprimir !=""):
        #exibindo a mensagem de erro
        pr.imprimir(erro_para_imprimir,cor_texto="vermelho negrito",tamanho=120,alinhar="centro")
        pr.separador(120,cor_texto="azul")
        
#Preparando a função de imprir o rodapé e pegar o comando que vai ser digitado
def imprimir_rodape():
     #imprimo o rodapé
     pr.imprimir("[S]Sair","[H] Ajuda",tamanho=120,alinhar="fim",caracter="─",end="┤")
     #pego o comando digitado mas sempre ele no formato minusculo (por isso a função lower)
     return input().lower()

#Preparando a função para imprimir a tela inicial
def imprimir_tela_inicial():
    #imprimindo o texto da tela inicial
    pr.pular_linha(quantidade=2)
    pr.imprimir('Tela inicial',tamanho=120,alinhar='centro')
    pr.pular_linha(quantidade=2)
#Preparando a função para imprimir a tela de ajuda
def imprimir_tela_ajuda():
    #imprimindo o texto de ajuda
    pr.pular_linha(quantidade=2)
    pr.imprimir('[H] - Abre a tela de ajuda com todos os comandos', tamanho=120)
    pr.imprimir('[S] - Fecha o sistema inteiro',tamanho=120)
    pr.imprimir('[N] - Abre uma nova compra')
    pr.imprimir('[nn] - Adiciona o codigo nn que foi passado na compra')
    pr.imprimir('[F]  - Fechar a compra que está em aberto')
    pr.imprimir('[P]  - Compra foi paga')
    pr.pular_linha(quantidade=2)
#Preparando a função para uma nova compra

def imprimir_nova_compra(compra):
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
        pr.imprimir('R$',str(item['valor']),tamanho=12,end='│',alinhar='fim')
        pr.imprimir('R$',str(item['valor'] * item['quantidade']),tamanho=12,alinhar='fim')
        subtotal += item['valor'] * item['quantidade']
    pr.separador(120,caracter='─')
    pr.imprimir('Subtotal',tamanho=107,end='│',alinhar='fim')
    pr.imprimir('R$',str(subtotal),tamanho=12,alinhar='fim')


#Declarando e inicializando as variáveis que vamos usar no controle das telas e dos comandos
opcao=""
erro=""
tela=""
compra=[]
#Definindo nosso laço de repetição, cada vez que esse laço executar é uma interação que 
while ((opcao != "s") and (opcao !="sair")):
    #imprimir cabeçalho e o erro
    imprimir_cabecalho(erro)
    erro=""

    #seleciono a tela que será exibida
    if(tela == ""):
        #Chamo a função da tela inicial
        imprimir_tela_inicial()
    elif(tela =="ajuda"):
        #Chamo a função da tela ajuda
        imprimir_tela_ajuda()
        #Sempre voltar para tela inicial depois que passar pela tela de ajuda
        tela=""
    elif(tela =="nova"):
        #Chamo a função da tela nova compra
        imprimir_nova_compra(compra)
        #chama a função que imprimi o rodapé e lê o comando digitado pelo usuária
    opcao= imprimir_rodape()
    #analiso o comando que foi digitado e tomo a decisão
    if(opcao == "h"):
        #se for "h" seta a variável de tela para entrar na tela de ajuda
        tela= "ajuda"
    elif(opcao == "n"):
        #Se for "n" seta a variável de tela para entrar na tela de nova compra
        tela = "nova"
    else:
        # se não for nenhum comando válido da uma mensagem de erro
        erro = "A opção não existe"

        
    
