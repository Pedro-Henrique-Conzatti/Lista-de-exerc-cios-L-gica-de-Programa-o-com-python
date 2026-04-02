nome = str(input("Nome do Clinte: "))
valorProduto = 0.0
valorTotal = 0.0
opcao = 1


while opcao == 1:
    print("O que você deseja?\n1 - Adicionar produto\n0 - Finalizar compra")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        # preciso pedir o valor do produto que ele quer rediricionar
        valorProduto = float(input("Valor do produto: R$: "))
        # depois preciso somar isso ao valor total da compra
        valorTotal = valorTotal + valorProduto
    elif opcao == 0:
        print(nome, "você deve pagar R$", valorTotal)

