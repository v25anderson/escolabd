from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime
from lists.lista_cursos import lista_curso
from lists.lista_professores import lista_professor

db = mysql.connect(host="localhost", user="root",
                   password="", database="escola")
command_handler = db.cursor(buffered=True)


def auth_turma():
    while 1:
        print("")
        print("AREA Turmas")
        print("")
        print("1. Registrar turmas")
        print("2. Deletar turmas")
        print("3. Listar turmas")
        print("4. Sair")

        user_option = input(str("Opcao: "))
        # CADASTRAR
        if user_option == "1":
            print("")
            print("Registrar Novo turmass")
            lista_professor()
            professores_id = input(str("Id do professor "))
            lista_curso()
            cursos_id = input(str("Id Curso "))
            data_inicio = input(str("Data inicio turma(yyyy-mm-aa): "))
            data_final = input(str("Data final turma(yyyy-mm-aa): "))
            carga_horaria = input(str("Carga Horaria: "))

            query_vals = (professores_id, cursos_id,
                          data_inicio, data_final, carga_horaria)
            command_handler.execute(
                "INSERT INTO turmas (professores_id, cursos_id, data_inicio, data_final, carga_horaria) VALUES (%s,%s,%s,%s,%s)", query_vals)
            db.commit()
            print("Turma Registrada")

          # DELETAR CONTA
        elif user_option == "2":
            print("")
            print("Deletar Conta de turmass Existente")
            nome = input(str("Nome do turmas: "))
            query_vals = (nome, "")
            command_handler.execute(
                "DELETE FROM turmas WHERE nome = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Usuario nao encontrado.")
            else:
                print(nome + " foi deletado com sucesso.")
           # LISTAR CONTAS
        elif user_option == "3":
            print("")
            print("Listar turmass")
            command_handler.execute("SELECT * FROM turmas")
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
