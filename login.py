import os,pymysql

os.system('cls' if os.name == 'nt' else 'clear')

def login(username_input, password_input):
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
        cursor.execute(consulta_sql, (username_input, password_input))

        usuario = cursor.fetchone()

        if usuario:
            nome_usuario= usuario[1]
            print(f"Bem-vindo, {nome_usuario}!")
            return True
        else:
            print("Nome de usuário ou senha incorretos.")
            return False

    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao MySQL: {e}")

    finally:
        if conexao:
            cursor.close()
            conexao.close()
            print("Conexão encerrada.")

username = input("Digite o nome de usuário: ")
password = input("Digite a senha: ")

login(username, password) 