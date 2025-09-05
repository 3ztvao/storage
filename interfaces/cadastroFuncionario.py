import os 
from PyQt5 import uic
from database import executar_sql,campos_vazios

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TelaCadastroFuncionario:
    def __init__(self):
        self.ui=uic.loadUi(os.path.join(BASE_DIR,"resources","cadastro","cadastro.ui"))
        self.ui.pushButton.clicked.connect(self.funcao_cadastroFuncionario)
        self.ui.show()
    
    def funcao_cadastroFuncionario(self):
        try:
            nome = self.ui.user_5.text().strip()
            username = self.ui.user_2.text().strip()
            cargo = self.ui.comboBox.currentText().strip()
            cpf = self.ui.user_7.text().strip()
            senha = self.ui.user_3.text().strip()
            sv = self.ui.user_4.text().strip()
            if campos_vazios(nome,username,cargo,cpf,senha,sv):
                self.ui.label_2.setText("Erro: Preencha todos os campos obrigatorios")
                self.ui.exito.setText("")
                return
            if senha != sv:
                self.ui.label_2.setText("As senhas digitadas não correspondem. Por favor, tente novamente.")
                self.ui.exito.setText("")
                return
        
            consulta_sql = "INSERT INTO usuarios (nome, cargo, login, senha, cpf) VALUES (%s, %s, %s, %s,%s)"
            parametros = (nome, cargo, username, senha,cpf)
            resultado = executar_sql(consulta_sql, parametros)
        
            if resultado is not None:
                self.ui.exito.setText("Cadastro realizado com sucesso!")
                self.ui.label_2.setText("")
                self.ui.user_5.clear()
                self.ui.user_2.clear()
                self.ui.user_6.clear()
                self.ui.user_7.clear()
                self.ui.user_3.clear()
                self.ui.user_4.clear()
            else:
               self.ui.label_2.setText("Erro ao realizar Cadastro. Verifique os dados.")
        except Exception as e:
            print(f"Erro no self.ui: {e}")
            self.ui.label_2.setText(f"Erro: {str(e)}")