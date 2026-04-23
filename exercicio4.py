#Crie uma aplicação que gera uma folha de pagamento de um funcionário de uma concessionária. 
#Esse software precisa mostrar na folha de pagamento o nome completo, 
#CPF e outras 2 informações que ficará à critério do desenvolvedor. 
#Antes da folha ser gerada, o usuário precisa informar também o salário base do funcionário, 
#quantos automóveis ele vendeu no mês, o percentual ganho por comissão por automóveis vendido 
#(ex: cada automóvel vendido equivale à uma comissão de 7% do salário naquele mês), 
#além de outros benefícios (como vale-alimentação e vale-transporte). 
#No final esse software deve exibir todas essas informações da seguinte forma:
#==========================
#NOME DO FUNCIONÁRIO COMPLETO | CPF DO FUNCIONÁRIO
#INFORMAÇÃO EXTRA 1 | INFORMAÇÃO EXTRA 2
#==========================
#SALÁRIO BASE DO FUNCIONÁRIO
#QUANTIDADE DE VEÍCULOS VENDIDOS NO MÊS
#PERCENTUAL DE COMISSÃO POR VEÍCULO VENDIDO (% EXTRA DO SALÁRIO)
#VALOR EM REAIS (R$) GANHO DE COMISSÃO
#VALOR EM REAIS (R$) GANHO DE VALE TRANSPORTE
#VALOR EM REAIS (R$) GANHO DE VALE ALIMENTAÇÃO
#VALOR EM REAIS (R$) TOTAL À RECEBER

nome_completo = str(input("Insira seu nome completo: "))
cpf = str(input("Insira seu CPF: "))
numero_chassi_carro = float(input("Insira seu numero de chassi do carro: "))
matricula_escolar = int(input("Insira sua matricula escolar: "))
salario_base = float(input("Insira seu salario base: "))
qtd_carros_vendidos = int(input("Insira quantidades de carros vendidos: "))
percentual_comicao = float(input("Insira o percentual de comição: "))
vale_alimentacao = float(input("Insira o valor do vale-alimentação: "))
vale_transporte = float(input("Insira o valor do vale-transporte: "))
valor_comicao = qtd_carros_vendidos * percentual_comicao

print("NOME DO FUNCIONÁRIO COMPLETO: ", nome_completo, "|" ,"CPF DO FUNCIONÁRIO: ", cpf)
print("INFORMAÇÃO EXTRA 1: ", numero_chassi_carro, "|" , matricula_escolar, "INFORMAÇÃO EXTRA 2:")
print("==================================")
print("SALÁRIO BASE DO FUNCIONÁRIO:", salario_base)
print("QUANTIDADE DE VEÍCULOS VENDIDOS NO MÊS", qtd_carros_vendidos)
print("PERCENTUAL DE COMISSÃO POR VEÍCULO VENDIDO (% EXTRA DO SALÁRIO)", percentual_comicao)
print("VALOR EM REAIS (R$) GANHO DE COMISSÃO", qtd_carros_vendidos * percentual_comicao)
print("seu valor em vale-transporte é:", vale_transporte)
print("seu valor em vale-alimentação é:", vale_alimentacao)
print("#VALOR EM REAIS (R$) TOTAL À RECEBER", salario_base + vale_alimentacao + vale_transporte + valor_comicao)
