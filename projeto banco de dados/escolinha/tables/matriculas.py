from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime
from lists.lista_alunos import lista_aluno
from lists.lista_turma import lista_turma


db = mysql.connect(host="localhost", user="root",
                   password="", database="escola")
command_handler = db.cursor(buffered=True)


def auth_matricula():
    while 1:
        print("")
        print("AREA MATRICULAS")
        print("")
        print("1. Registrar Matricula")
        print("2. Deletar Matriculas")
        print("3. Sair")

        user_option = input(str("Opcao: "))
        # CADASTRAR
        if user_option == "1":
            print("")
            print("Registrar Novo Matriculas")
            lista_turma()
            turmas_id = input(str("Id da turma "))
            lista_aluno()
            alunos_id = input(str("Id Aluno "))
            data_matricula = input(str("Data matricula(yyyy-mm-aa): "))
            query_vals = (turmas_id, alunos_id, data_matricula)
            command_handler.execute(
                "INSERT INTO matriculas (turmas_id, alunos_id, data_matricula) VALUES (%s,%s,%s)", query_vals)
            db.commit()
            print(" Matricula Registrada")

          # DELETAR CONTA
        elif user_option == "2":
            print("")
            print("Deletar  Matricula Existente")
            id = input(str("Id da Matricula: "))
            query_vals = (id, "")
            command_handler.execute(
                "DELETE FROM matriculas WHERE id = %s OR data_matricula = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Usuario nao encontrado.")
            else:
                print("Matricula" + id + " foi deletada com sucesso.")

        elif user_option == "3":
            break
        else:
            print("Opcao selecionada nao valida")
