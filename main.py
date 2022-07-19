from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(host="localhost", user="root",
                   password="", database="escola")
command_handler = db.cursor(buffered=True)


def main():
    while 1:
        print("")
        print("MENU ADMIN")
        print("")
        print("1. Registrar Estudante")
        print("2. Deletar Estudante")
        print("3. Listar Estudantes")
        print("4. Sair")

        user_option = input(str("Opcao: "))
        # CADASTRAR
        if user_option == "1":
            print("")
            print("Registrar Novo Estudante")
            nome = input(str("Nome do Estudante: "))
            cpf = input(str("CPF do Estudante: "))
            email = input(str("Email do Estudante: "))
            fone = input(str("Telefone do Estudante: "))

            query_vals = (nome, cpf, email, fone)
            command_handler.execute(
                "INSERT INTO alunos (nome, cpf, email,fone) VALUES (%s,%s,%s,%s)", query_vals)
            db.commit()
            print(nome + " registrado como estudante.")

          # DELETAR CONTA
        elif user_option == "2":
            print("")
            print("Deletar Conta de Estudante Existente")
            nome = input(str("Nome do estudante: "))
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
            print("Listar Estudantes")
            command_handler.execute("SELECT * FROM alunos")
            dados_lidos = command_handler.fetchall()
            for i in range(0, len(dados_lidos)):
                for j in range(0, 5):
                    print(dados_lidos[i][j])

        elif user_option == "4":
            break
        else:
            print("Opcao selecionada nao valida")


main()
