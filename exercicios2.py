#Crie uma aplicação que recebe o nome, a turma, a matéria desejada e as notas do estudante. 
#ENQUANTO o usuário não finalizar a inserção de novas notas, ele somará elas. 
#Caso ele não queira mais passar nenhuma nova nota, 
#o código deve dividir a soma pela quantidade de notas. 
#O código deve informar se o aluno passou, reprovou ou se está em exame.


nome = str(input("Nome do Aluno: "))
turma = str(input("Nome da turma: "))
materia = str(input("Matéria: "))
NotasDoEstudante = float(input("Notas: "))
SomaDasNotas = float(input("Soma de Todas as notas: "))
QuantidadesDeNotas = float(input("Quantidade de notas: "))

while opcao == 1:
    print("O que você deseja?\n1 - Adicionar notas\n0 - Terminar média")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        # preciso pedir o valor do produto que ele quer rediricionar
        NotasDoEstudante = float(input("Insira uma nota: "))
        # depois preciso somar isso ao valor total da compra

    elif opcao == 0:
        print(nome, "você deve pagar R$", valorTotal)


