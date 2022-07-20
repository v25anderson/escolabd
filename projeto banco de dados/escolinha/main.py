from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime
from tables.cursos import auth_curso
from tables.professor import auth_prof
from tables.alunos import auth_aluno
from tables.matriculas import auth_matricula
from tables.turmas import auth_turma


def principal():
    while 1:
        print("")
        print("Bem-vindo ao sistema escolar")
        print("")
        print("1. Area dos alunos")
        print("2. Area dos professores")
        print("3. Area dos cursos")
        print("4. Area das matriculas")
        print("5. Area das turmas")
        print("6. Sair")

        user_option = input(str("Opcao: "))
        if user_option == "1":
            auth_aluno()
        elif user_option == "2":
            auth_prof()
        elif user_option == "3":
            auth_curso()
        elif user_option == "4":
            auth_matricula()
        elif user_option == "5":
            auth_turma()
        elif user_option == "6":
            break
        else:
            print("Opcao selecionada nao valida.")


principal()
