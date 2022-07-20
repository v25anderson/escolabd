from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(host="localhost", user="root",
                   password="", database="escola")
command_handler = db.cursor(buffered=True)


def auth_prof():
    while 1:
        print("")
        print("AREA PROFESSOR")
        print("")
        print("1. Registrar Professor")
        print("2. Deletar Professor")
        print("3. Listar Professor")
        print("4. Sair")

        user_option = input(str("Opcao: "))
        # CADASTRAR
        if user_option == "1":
            print("")
            print("Registrar Novo Professor")
            nome = input(str("Nome do Professor: "))
            email = input(str("Email do Professor: "))
            valor = input(str("Valor Hora do Professor: "))
            certificado = input(str("Certificados do Professor: "))

            query_vals = (nome, email,  valor, certificado)
            command_handler.execute(
                "INSERT INTO professores (nome, email, valor_hora, certificados) VALUES (%s,%s,%s,%s)", query_vals)
            db.commit()
            print(nome + " registrado como Professor.")

          # DELETAR CONTA
        elif user_option == "2":
            print("")
            print("Deletar Conta de Professor Existente")
            nome = input(str("Nome do Professor: "))
            query_vals = (nome, "")
            command_handler.execute(
              
                "DELETE FROM professores WHERE nome = %s OR email = %s", query_vals)
              
            db.commit()
            if command_handler.rowcount < 1:
                print("Usuario nao encontrado.")
            else:
                print(nome + " foi deletado com sucesso.")
           # LISTAR CONTAS
        elif user_option == "3":
            print("")
            print("Listar Professors")
            command_handler.execute("SELECT * FROM professores")
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
