from database import executar_sql, campos_vazios
import os
from utils import carregar_combo_boxes_tela
from PyQt5 import uic, QtWidgets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAMINHO_UI = os.path.join(BASE_DIR, 'resources', 'cadastro', 'cadastroColecao.ui')

class TelaCadastroColecao(QtWidgets.QWidget):
    def __init__(self, tela_produto=None):
        super().__init__()
        uic.loadUi(CAMINHO_UI, self)
        self.tela_produto = tela_produto
        self.pushButton.clicked.connect(self.cadastrar_Colecao)
        self.show()

    def cadastrar_Colecao(self):
        try:
            nome = self.nomeColecao.text().upper().strip()
            sigla = self.siglaColecao.text().upper().strip()
            ano = self.ano.value()

            if campos_vazios(nome, sigla):
                self.correto.setText("Erro: Preencha todos os campos obrigatórios")
                self.exito.setText("")
                return

            consulta_sql = "INSERT INTO colecao (nome_colecao, sigla_colecao, ano) VALUES (%s, %s, %s)"
            parametros = (nome, sigla, ano)
            resultado = executar_sql(consulta_sql, parametros)

            if resultado is not None:
                self.correto.setText("Cadastro realizado com sucesso!")
                self.nomeColecao.clear()
                self.siglaColecao.clear()
                self.ano.setValue(0)

                if self.tela_produto:
                    self.tela_produto.atualizar_combos()
            else:
                self.error.setText("Erro ao realizar cadastro. Verifique os dados.")
        except Exception as e:
            print(f"[ERRO] Erro no cadastro: {e}")
            self.error.setText(f"Erro: {str(e)}")