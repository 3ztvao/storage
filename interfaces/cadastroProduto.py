
import os, random
from PyQt5 import uic
from database import executar_sql,campos_vazios
from utils import carregar_combo_boxes_tela, carregar_todas_combo_box

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TelaCadastroProduto:
    def __init__(self):
        self.ui=uic.loadUi(os.path.join(BASE_DIR,"resources","cadastro","cadastroProduto.ui"))
        self.carregar_dados()
        self.ui.pushButton.clicked.connect(self.cadastrarProduto)
        self.ui.criarColecao.clicked.connect(self.abrir_tela_cadastroColecao)
        self.ui.criarModelo.clicked.connect(self.abrir_tela_cadastroModelo)
        self.ui.criarVariacao.clicked.connect(self.abrir_tela_cadastroVariacao)
        self.ui.show()
    def atualizar_combos(self):
        from utils import carregar_combo_boxes_tela
        carregar_combo_boxes_tela(self, {
            "colecao": "colecao",  
            "modelo": "modelo",
            "variacao": "variacao"
    })
    def carregar_dados(self):
        carregar_combo_boxes_tela(self.ui, 'TelaCadastroProduto')
    def cadastrarProduto(self):
        mod = self.ui.modelo.currentText().strip()
        col = self.ui.col.currentText().strip()
        nomePeca=self.ui.nome.text().strip()
        obs = self.ui.obs.currentText().strip()
        preco_texto=self.ui.preco.text().strip()

        if not (mod and col and nomePeca and preco_texto):
            self.ui.erromensage.setText(None, "Erro", "Preencha todos os campos obrigatórios.")
            return

        try:
            preco_texto = float(preco_texto.replace(',', '.'))
        except ValueError:
            self.ui.erromensage.setText(None, "Erro", "Preço inválido.")
            return

        ref = f"{mod[:3]}-{col[:2]}-{obs}-{random.randint(1000,9999)}".lower()
    
    def abrir_tela_cadastroModelo(self):
        from interfaces.cadastros.cadastro_modelo import TelaCadastroModelo
        print("Abrindo TelaCadastroModelo...")
        try:
            self.tela_cadastroModelo=TelaCadastroModelo()
            self.tela_cadastroModelo.ui.show()
        except Exception as e:
            print("Erro ao abrir TelaCadastroModelo",e)
    
    def abrir_tela_cadastroColecao(self):
        from interfaces.cadastros.cadastro_colecao import TelaCadastroColecao
        print("Abrindo TelaCadastroColecao...")
        try:
            self.telaCadastroColecao = TelaCadastroColecao(tela_produto=self)
            self.tela_cadastroColecao.ui.show()
        except Exception as e:
            print("Erro ao abrir TelaCadastroColecao:", e)
    def abrir_tela_cadastroVariacao(self):
        from interfaces.cadastros.cadastro_variacao import TelaCadastroVariacao
        try:
            self.tela_cadastroVariacao= TelaCadastroVariacao()
            self.tela_cadastroVariacao.ui.show()
        except Exception as e:
            print("Erro ao abrir TelaCadastroVariacao",e)