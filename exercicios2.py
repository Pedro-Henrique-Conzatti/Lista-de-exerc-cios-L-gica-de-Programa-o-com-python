#Crie uma aplicação que recebe o nome, a turma, a matéria desejada e as notas do estudante. 
#ENQUANTO o usuário não finalizar a inserção de novas notas, ele somará elas. 
#Caso ele não queira mais passar nenhuma nova nota, 
#o código deve dividir a soma pela quantidade de notas. 
#O código deve informar se o aluno passou, reprovou ou se está em exame.


nome = str(input("Nome do Aluno: "))
turma = str(input("Nome da turma: "))
materia = str(input("Matéria: "))
notas = 0.0
qtd_notas = 0
opcao_tela = 1

while opcao_tela == 1:
    opcao_tela = int(input("O que você deseja?\n[1] - Adicionar nota\n[0] - Sair\nOpção: "))
    if opcao_tela == 1:
       qtd_notas += 1
       nova_nota = float(input(f"{qtd_notas}ª nota do estudante: "))
       notas = notas + nova_nota
    else:
        print("Média = ", notas / qtd_notas)
        if notas >= 6:
            print("Você passou")
        if notas <= 6:
            print("Você esta em exame")
        if notas <= 4:
            print("Você reprovou")
    
