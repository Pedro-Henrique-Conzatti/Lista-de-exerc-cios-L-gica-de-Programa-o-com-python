# Crie uma aplicação que faz a gestão de estoque de uma empresa. 
# Essa empresa precisa ter um produto, uma descrição para este produto, ✔
# um número x de um dado produto, ✔
# o valor unitário de cada produto e o valor total do estoque. ✔
# O software deve permitir atualizarmos  ✔
# o valor do produto (refletindo no valor total do estoque), ✔
# atualizar a quantidade do produto em estoque, 
# atualizar o nome do produto e 
# atualizar a descrição deste produto. 
# Por fim, o software deve permitir também que a gente possa ver essas informações.

Produto = str(input("Insira o nome do produto: "))
DescriçãoProduto = str(input("Descreva o seu produto: "))
QuantidadeProduto = int(input("Insira a quantidade do seu produto: "))
ValorProduto = float(input("Insira o valor do seu produto: "))
ValorProdutoTotal = QuantidadeProduto * ValorProduto

opcao = 0

while opcao != 6:
    print("[1] - Ver informações do produto")
    print("[2] - Atualizar o nome do produto")
    print("[3] - Atualizar descrição")
    print("[4] - Atualizar quantidade em estoque do produto")
    print("[5] - Atualizar valor unitario do produto")
    print("[6] - Sair")
    opcao = int(input("Opção desejada: "))
    if opcao == 1:
        print("-------------------------")
        print("Nome: ", Produto , " | Valor R$: ", ValorProdutoTotal)
    elif opcao == 2:
        print("Nome do produto atual: ", Produto)
        Produto = str(input("Insira o novo nome do produto: "))
    elif opcao == 3:
        print("Descrição do produto: ", DescriçãoProduto)
        DescriçãoProduto = str(input("Descreva o seu produto: "))
    elif opcao == 4:
        print("Quantidade do produto: ",QuantidadeProduto)
        QuantidadeProduto = int(input("Insira a quantidade do seu produto: "))
    elif opcao == 5:
        ValorProduto = float(input("Insira o novo valor do produto: R$ "))
        ValorProdutoTotal = QuantidadeProduto * ValorProduto
        print("Valor unitario do produto: ", ValorProdutoTotal)
    elif opcao == 6:
        print("fim do programa")
        
