import os,pymysql
from PyQt5 import uic,QtWidgets

os.system('cls' if os.name == 'nt' else 'clear')

#Funçã para puxar no mysql
def login(username,password):
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='admin',
            database='loja'
        )
        print("Conexão estabelecida com sucesso!")

        cursor = conexao.cursor()

        consulta_sql = "SELECT * FROM usuarios WHERE login = %s AND senha = %s "
        cursor.execute(consulta_sql, (username, password))

        usuario = cursor.fetchone()

        if usuario:
            nome_usuario= usuario[1]
            print(f"Bem-vindo, {nome_usuario}!")
            janela2.show()
            return True
        else:
            print("Nome de usuário ou senha incorretos.")
            janela.error.setText("Nome de usuário ou senha incorretos.")

    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao MySQL: {e}")

    finally:
        if conexao:
            cursor.close()
            conexao.close()
            print("Conexão encerrada.")
#QtD
def funcao_principal():
    username=janela.user.text()
    password=janela.senha.text()
    login(username,password)
    janela.user.setText("")
    janela.senha.setText("")
    
        
    
app=QtWidgets.QApplication([])
janela=uic.loadUi("janela.ui")
janela2=uic.loadUi("janela2.ui")
janela.pushButton.clicked.connect(funcao_principal)
janela.show()
app.exec()