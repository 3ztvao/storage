import pymysql
import os
os.system('cls' if os.name == 'nt' else 'clear')
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

def campos_vazios(*campos):
    return any(not campo.strip() for campo in campos)