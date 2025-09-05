from database import executar_sql,campos_vazios
import os
from PyQt5 import uic
from utils import carregar_combo_box,carregar_combo_boxes_tela,carregar_todas_combo_box

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TelaCadastroVariacao:
    def __init__(self):
        print("abrindo TelaCadastroVariacao")
        caminho_ui = os.path.join(BASE_DIR,"resources","cadastro","cadastroVariacao.ui")
        self.ui=uic.loadUi(caminho_ui)
        self.ui.pushButton.clicked.connect(self.cadastrar_Variacao)
        self.ui.show()
    def cadastrar_Variacao(self):
        try:
            nome = self.ui.nome.text().strip().upper()
            sigla = self.ui.siglaVariacao.text().strip().upper()
            if campos_vazios(nome,sigla):
                self.ui.errorlabel.setText("Erro: Preencha todos os campos obrigatorios")
                return
            consulta_sql=("INSERT INTO variacao(nome_variacao,sigla_variacao)VALUES(%s,%s)")
            parametros =(nome,sigla)
            resultado = executar_sql(consulta_sql,parametros)

            if resultado is not None:
                self.ui.errorlabel.setText("Cadastro realizado com sucesso!")
                self.ui.nome.clear()
                self.ui.siglaVariacao.clear()
                carregar_combo_boxes_tela(self.ui)
                carregar_todas_combo_box()
            else:
                self.ui.errorlabel.setText("Erro ao realizar o cadastro. Verifique os dados.")
        except Exception as e:
            print(f"[ERRO] Erro no cadastro: {e}")
            self.ui.errorlabel.setText(f"Erro: {str(e)}")