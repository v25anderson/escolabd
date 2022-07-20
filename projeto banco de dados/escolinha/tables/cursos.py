from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(host="localhost", user="root",
                   password="", database="escola")
command_handler = db.cursor(buffered=True)


def auth_curso():
    while 1:
        print("")
        print("AREA CURSOS")
        print("")
        print("1. Registrar Curso")
        print("2. Deletar Curso")
        print("3. Listar Cursos")
        print("4. Sair")

        user_option = input(str("Opcao: "))
        # CADASTRAR
        if user_option == "1":
            print("")
            print("Registrar Novo Curso")
            nome = input(str("Nome do Curso: "))
            carga = input(str("Carga Horaria do Curso: "))

            query_vals = (nome, carga)
            command_handler.execute(
                "INSERT INTO cursos (nome, carga_horaria) VALUES (%s,%s)", query_vals)
            db.commit()
            print(nome + " registrado como Curso.")

          # DELETAR CONTA
        elif user_option == "2":
            print("")
            print("Deletar Curso Existente")
            nome = input(str("Nome do Curso: "))
            query_vals = (nome, "")
            command_handler.execute(
                "DELETE FROM  cursos WHERE nome = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Usuario nao encontrado.")
            else:
                print(nome + " foi deletado com sucesso.")
           # LISTAR CONTAS
        elif user_option == "3":
            print("")
            print("Listar Cursos")
            command_handler.execute("SELECT * FROM cursos")
            dados_lidos = command_handler.fetchall()
            for i in range(0, len(dados_lidos)):
                print("\n")
                print("#################")
                for j in range(0, 2):
                    print(dados_lidos[i][j])

        elif user_option == "4":
            break
        else:
            print("Opcao selecionada nao valida")
