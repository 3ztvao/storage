import os,pymysql

os.system('cls'if os.name =='nt'else 'clear')

def cadastro(nome,cargo,acesso,login,senha):
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='admin',
            database='loja'
        )
        print("Conexão estabelecida com sucesso!")

        cursor = conexao.cursor()

        inserir_sql = "INSERT INTO usuarios(Nome,Cargo,acesso,login,senha)VALUES(nome,cargo,acesso,login,senha)"
    
    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao MySQL: {e}")

    finally:
        if conexao:
            cursor.close()
            conexao.close()
            print("Conexão encerrada.")

cadastro()