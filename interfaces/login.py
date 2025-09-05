import random
import os
from PyQt5 import uic, QtWidgets
from database import executar_sql, campos_vazios
from interfaces.tela_principal import TelaPrincipal

# Limpar o terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Definindo o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TelaLogin:
    def __init__(self):
        self.ui = uic.loadUi(os.path.join(BASE_DIR, "resources", "login", "main.ui"))
        self.ui.pushButton.clicked.connect(self.verificar_login)
        self.ui.show()

    def verificar_login(self):
            username = self.ui.user.text().strip()
            senha = self.ui.senha.text().strip()
            self.login(username, senha)
    
    def login(self,username, senha):
            consulta_sql = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"
            parametros = (username, senha)
            resultado = executar_sql(consulta_sql, parametros)
            if resultado:
                consulta_cargo = "SELECT cargo FROM usuarios WHERE login = %s"
                cargo = executar_sql(consulta_cargo, (username,))
                if cargo:
                    self.tela_principal = TelaPrincipal(cargo[0][0])  
                    self.tela_principal.show()
                    self.ui.close()
            else:
                self.ui.error.setText("Nome de usuário ou senha incorretos.")
                self.ui.user.clear()
                self.ui.senha.clear()
                return False