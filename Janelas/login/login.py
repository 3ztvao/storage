import os
import pymysql
from PyQt5 import uic, QtWidgets

os.system('cls' if os.name == 'nt' else 'clear')

# Função para conectar ao MySQL 
def conectar_db():
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='admin',
            database='loja',
            charset='utf8mb4'  
        )
        print("Conexão estabelecida com sucesso!")
        return conexao
    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao MySQL: {e.args}")  
        return None

# Função para executar comandos SQL 
def executar_sql(consulta_sql, parametros=None):
    conexao = conectar_db()
    if conexao is None:
        return None
    try:
        cursor = conexao.cursor()
        if parametros:
            cursor.execute(consulta_sql, parametros)
        else:
            cursor.execute(consulta_sql)

        # Para comandos de inserção, atualização ou exclusão
        if "INSERT" in consulta_sql or "UPDATE" in consulta_sql or "DELETE" in consulta_sql:
            conexao.commit()
            return cursor.lastrowid

        return cursor.fetchall()  
    except pymysql.MySQLError as e:
        print(f"Erro ao executar consulta SQL: {e.args}") 
        return None
    finally:
        cursor.close()
        conexao.close()

# Função para puxar no MySQL
def login(username, senha): 
    consulta_sql = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"
    parametros = (username, senha)
    resultado = executar_sql(consulta_sql, parametros)

    if resultado and len(resultado) > 0:
        janela2.show()
        janela.close()
        return True
    else:
        janela.error.setText("Nome de usuário ou senha incorretos.")
        janela.user.clear()
        janela.senha.clear()
        return False 

# Função principal de login
def funcao_principal():
    username = janela.user.text().strip() 
    senha = janela.senha.text().strip()
    print(f"Usuário: {username}, Senha: {senha}")
    login(username, senha)  

# Função para abrir a janela de cadastro
def funcao_cadastro():
    cadastro.show()
    janela.close()
    janela2.close()

# Função para realizar cadastro
def Sing():
    try:
        nome = cadastro.user_5.text().strip()
        username = cadastro.user_2.text().strip()
        cargo = cadastro.user_6.text().strip()
        cpf = cadastro.user_7.text().strip()
        senha = cadastro.user_3.text().strip()
        sv = cadastro.user_4.text().strip()

        # Verificação se as senhas são iguais
        if senha != sv:
            cadastro.label_2.setText("As senhas digitadas não correspondem. Por favor, tente novamente.")
            return
        
    
        consulta_sql = "INSERT INTO usuarios (login, senha, nome, cargo, cpf) VALUES (%s, %s, %s, %s, %s)"
        parametros = (username, senha, nome, cargo, cpf)
        
        resultado = executar_sql(consulta_sql, parametros)
        
        if resultado is not None:
            cadastro.label_2.setText("Cadastro realizado com sucesso!")
            # Limpar os campos
            cadastro.user_5.clear()
            cadastro.user_2.clear()
            cadastro.user_6.clear()
            cadastro.user_7.clear()
            cadastro.user_3.clear()
            cadastro.user_4.clear()
        else:
            cadastro.label_2.setText("Erro ao realizar cadastro. Verifique os dados.")
    except Exception as e:
        print(f"Erro no cadastro: {e}")
        cadastro.label_2.setText(f"Erro: {str(e)}")  # Mostra o erro na interface para facilitar o debug
        

# Declarando telas
app = QtWidgets.QApplication([])
janela = uic.loadUi(r"c:\Users\Eztevao\Documents\Proz\storage\janelas\login\janela.ui")
janela2 = uic.loadUi(r"c:\Users\Eztevao\Documents\Proz\storage\janelas\inicial\janela2.ui")
cadastro = uic.loadUi(r"c:\Users\Eztevao\Documents\Proz\storage\janelas\cadastro\cadastro.ui")

janela.pushButton.clicked.connect(funcao_principal)
janela2.pushButton.clicked.connect(funcao_cadastro)
cadastro.pushButton.clicked.connect(Sing)
janela.pushButton_2.clicked.connect(funcao_cadastro)

janela.show()
app.exec()