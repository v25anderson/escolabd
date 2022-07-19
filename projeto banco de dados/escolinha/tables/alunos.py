from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(host="localhost", user="root",
                   password="", database="escola")
command_handler = db.cursor(buffered=True)


def auth_aluno():
    while 1:
        print("")
        print("AREA DOS ALUNOS")
        print("")
        print("1. Registrar Alunos")
        print("2. Deletar Alunos")
        print("3. Listar Alunos")
        print("4. Sair")

        user_option = input(str("Opcao: "))
        # CADASTRAR
        if user_option == "1":
            print("")
            print("Registrar Novo Alunos")
            nome = input(str("Nome do Alunos: "))
            cpf = input(str("CPF do Alunos: "))
            email = input(str("Email do Alunos: "))
            fone = input(str("Telefone do Alunos: "))

            query_vals = (nome, cpf, email, fone)
            command_handler.execute(
                "INSERT INTO alunos (nome, cpf, email,fone) VALUES (%s,%s,%s,%s)", query_vals)
            db.commit()
            print(nome + " registrado como Alunos.")

          # DELETAR CONTA
        elif user_option == "2":
            print("")
            print("Deletar Conta de Alunos Existente")
            nome = input(str("Nome do Alunos: "))
            query_vals = (nome, "")
            command_handler.execute(
                "DELETE FROM alunos WHERE nome = %s OR cpf = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Usuario nao encontrado.")
            else:
                print(nome + " foi deletado com sucesso.")
           # LISTAR CONTAS
        elif user_option == "3":
            print("")
            print("Listar Alunoss")
            command_handler.execute("SELECT * FROM alunos")
            dados_lidos = command_handler.fetchall()
            for i in range(0, len(dados_lidos)):
                print("\n")
                print("#################")
                for j in range(0, 5):
                    print(dados_lidos[i][j])

        elif user_option == "4":
            break
        else:
            print("Opcao selecionada nao valida")
