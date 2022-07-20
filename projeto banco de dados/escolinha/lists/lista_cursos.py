from matplotlib.style import use
import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(host="localhost", user="root",
                   password="", database="escola")
command_handler = db.cursor(buffered=True)
 
def lista_curso():
     
     print("")
     print("Listar Turmas")
     command_handler.execute("SELECT * FROM cursos")
     dados_lidos = command_handler.fetchall()
     for i in range(0, len(dados_lidos)):
                print("\n")
                print("#################")
                for j in range(0, 3):
                    print(dados_lidos[i][j])