from matplotlib.style import use
import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", password="", database="college")
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("MENU ADMIN")
        print("")
        print("1. Registrar Estudante")
        print("2. Registrar Professor")
        print("3. Deletar Estudante")
        print("4. Deletar Professor")
        print("5. Sair")
        
        user_option = input(str("Opcao: "))
        if user_option == "1":
            print("")
            print("Registrar Novo Estudante")
            username = input(str("Nome do Estudante: "))
            password = input(str("Senha do Estudante: "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s, 'estudante')", query_vals)
            db.commit()
            print(username + " registrado como estudante.")
        elif user_option == "2":
            print("")
            print("Registrar Novo Professor")
            username = input(str("Nome do Professor: "))
            password = input(str("Senha do Professor: "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s, 'professor')", query_vals)
            db.commit()
            print(username + " registrado como professor.")
            
        elif user_option == "3":
            print("")
            print("Deletar Conta de Estudante Existente")
            username = input(str("Nome do estudante: "))
            query_vals = (username,"estudante")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Usuario nao encontrado.")
            else:
                print(username + " foi deletado com sucesso.")       
        elif user_option == "4":
            print("")
            print("Deletar Conta de Professor Existente")
            username = input(str("Nome do professor: "))
            query_vals = (username,"professor")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Usuario nao encontrado.")
            else:
                print(username + " foi deletado com sucesso.")
                
        elif user_option == "5":
            break
        else:
            print("Opcao selecionada nao valida")

def teacher_session():
    while 1:
        print("")
        print("MENU PROFESSOR")
        print("")
        print("1. Marcacao de presenca")
        print("2. Vizualizar registro")
        print("3. Sair")

        user_option = input(str("Opcao: "))
        if user_option == "1":
            print("")
            print("Registrar presenca dos alunos")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'estudante'")
            records = command_handler.fetchall()
            date = input(str("Data: DD/MM/AAAA "))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")

                status = input(str("Status aluno: " + str(record) + " P/A: "))
                query_vals = (str(record),date,status)
                command_handler.execute("INSERT INTO attendance (username, date, status) VALUES(%s,%s,%s)", query_vals)
                db.commit()
                print(record + " Marcado com " + status)
        elif user_option == "2":
            print("")
            print("Ver o registro de presenca de todos os estudantes")
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print("Exibindo todos os registros de presenca")
            for record in records:
                print(record)
        elif user_option == 3:
            break
        else:
            print("Opcao selecionada nao valida.")

def student_session(username):
    while 1:
        print("")
        print("MENU ESTUDANTE")
        print("")
        print("1. Ver registro de frequencia")
        print("2. Baixar registro de frequencia")
        print("3. Sair")

        user_option = input(str("Opcao: "))
        if user_option == "1":
            username = (str(username),)
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username)
            records = command_handler.fetchall()
            for record in records:
                print(record)
        elif user_option == "2":
            print("")
            print("Baixando registro de frequencia.")
            print("")
            username = (str(username),)
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s", username)
            records = command_handler.fetchall()
            for record in records:
                with open("C:/Users/Thiago Raposo/Desktop/Faculdade/registro.txt", "w") as f:
                    f.write(str(records) + "\n")
                f.close()
            print("Todos os registros de frequencia foram salvos.")
        elif user_option == "3":
            break
        else:
            print("Opcao selecionada nao valida.")


def auth_admin():
    print("")
    print("Administrador Login")
    print("")
    username = input(str("Nome: "))
    password = input(str("Senha: "))
    if username == "admin":
        if password == "12345":
            admin_session()
        else:
            print("Senha incorreta.")
    else:
        print("Dados informados não foram reconhecidos pelo sistema.")

def auth_teacher():
    print("")
    print("Professor Login")
    print("")
    username = input(str("Nome: "))
    password = input(str("Senha: "))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'professor'", query_vals)
    if command_handler.rowcount <= 0:
        print("Usuario nao reconhecido.")
    else:
        teacher_session()

def auth_student():
    print("")
    print("Aluno Login")
    print("")
    username = input(str("Nome: "))
    password = input(str("Senha: "))
    query_vals = (username,password,"estudante")
    command_handler.execute("SELECT username FROM users WHERE username = %s AND password = %s AND privilege = %s", query_vals)
    if command_handler.rowcount <= 0:
        print("Usuario nao reconhecido.")
    else:
        student_session(username)


def main():
    while 1:
        print("")
        print("Bem-vindo ao sistema escolar da faculdade.")
        print("")
        print("1. Login para estudante")
        print("2. Login para professor")
        print("3. Login para admin")
        print("4. Sair")

        user_option = input(str("Opcao: "))
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_teacher()
        elif user_option == "3":
            auth_admin()
        elif user_option == "4":
            break
        else:
            print("Opcao selecionada nao valida.")

main()