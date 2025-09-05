import os, random
from database import executar_sql,campos_vazios
from PyQt5 import uic
from utils import carregar_combo_box,carregar_combo_boxes_tela, carregar_todas_combo_box
BASE_DIR =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TelaCadastroModelo:
    def __init__(self):
        caminho_ui=os.path.join(BASE_DIR,"resources","cadastro","cadastroModelo.ui")
        self.ui=uic.loadUi(caminho_ui)
        self.carregar_dados()
        self.ui.pushButton.clicked.connect(self.funcao_cadastroModelo)
        self.ui.criarTipo.clicked.connect(self.abrir_tela_cadastroTipo)
        self.ui.show()
    def carregar_dados(self):
        carregar_combo_boxes_tela(self.ui, 'TelaCadastroModelo')
    def abrir_tela_cadastroTipo(self):
        from interfaces.cadastros.cadastro_tipo import TelaCadastroTipo
        print("Abrindo TelaCadastroTipo...")
        try:
            self.tela_cadastroTipo=TelaCadastroTipo()
            self.tela_cadastroTipo.ui.show()
        except Exception as e:
            print("Erro ao abrir TelaCadastroTipo", e)
    def funcao_cadastroModelo(self):
        try:   
            nome = self.ui.nome.text().strip().upper()
            id_tipo= self.ui.tipoPeca.currentData()
            sigla = self.ui.siglaModelo.text().strip().upper()
            if campos_vazios(nome,sigla):
                self.ui.errorlabel.setText("Erro: Preenha Todos os campos obrigatorios")
                return 
            consulta_sql=("INSERT INTO modelo (nome_modelo,id_tipo,sigla_modelo)VALUES(%s,%s,%s)") 
            parametros =(nome,id_tipo,sigla)       

            resultado= executar_sql(consulta_sql,parametros)

            if resultado is not None:
                self.ui.errorLabel.setText("Cadastro realizado com sucesso!")
                self.ui.nome.clear()
                carregar_todas_combo_box()
                carregar_combo_boxes_tela(self.ui, 'TelaCadastroModelo')
                self.ui.siglaModelo.clear()
                self.ui.tipoPeca.setCurrentIndex(0)
            else:
                self.ui.errorLabel.setText("Erro ao Cadastrar modelo.")
        except Exception as e:
            self.ui.errorLabel.setText(f"Erro inesperado: {str(e)}")
            print(f"error: {e}")

