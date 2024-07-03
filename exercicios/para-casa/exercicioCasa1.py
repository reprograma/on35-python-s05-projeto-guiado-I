def obterItem():
    codigo = int(input("Digite o código do item: "))
    preco = float(input("Digite o preço do item: "))
    quantidade = 1

    entradaQuantidade = input("Digite a quantidade ou 'xQuantidade' para multiplicar: ")
    if entradaQuantidade.startswith("x"):
        try:
            quantidade = int(entradaQuantidade[1:])
        except ValueError:
            print("Quantidade inválida. Usando quantidade padrão (1).")
    
    return {'codigo': codigo, 'preco': preco, 'quantidade': quantidade}

def calcularTotalDesconto(itens):
    total = sum(item['preco'] * item['quantidade'] for item in itens)
    if total > 100:
        total *= 0.9

    codigos10 = [item['codigo'] for item in itens].count(10)
    if codigos10 > 1:
        total -= 0.5 * min(item['preco'] for item in itens if item['codigo'] == 10)

    return total

def cancelarItem(itens):
    codigoCancelar = int(input("Digite o código do item a ser cancelado: "))
    for item in itens:
        if item['codigo'] == codigoCancelar:
            itens.remove(item)
            print(f"Item com código {codigoCancelar} cancelado.")
            break
    else:
        print(f"Item com código {codigoCancelar} não encontrado na compra.")

numItens = int(input("Quantos itens na compra? "))
itensCompra = [obterItem() for _ in range(numItens)]

cancelarItem(itensCompra)  

totalDesconto = calcularTotalDesconto(itensCompra)
print(f"Total com desconto: R$ {totalDesconto:.2f}")