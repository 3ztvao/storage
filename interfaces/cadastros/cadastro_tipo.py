from database import executar_sql,campos_vazios
import os
from PyQt5 import uic, QtWidgets
from utils import carregar_combo_box,carregar_combo_boxes_tela,carregar_todas_combo_box

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TelaCadastroTipo:
    def __init__(self):
        print("TelaCadastroTipo")
        caminho_ui = os.path.join(BASE_DIR, "resources", "cadastro", "cadastroTipo.ui")
        self.ui = uic.loadUi(caminho_ui)
        self.ui.pushButton.clicked.connect(self.funcao_cadastroTipo)
        self.ui.show()

    def funcao_cadastroTipo(self):
        try:
            nome= self.ui.nome.text().strip().upper()
            siglaTipo = self.ui.siglaTipo.text().strip().upper()
            padraoGrade = self.ui.padraoGrade.currentText().strip().upper()
            publico= self.ui.publico.currentText().strip().upper()
            if campos_vazios(nome,siglaTipo,padraoGrade,publico):
                self.ui.errorlabel.setText("Erro: Preenca todos os campos obrigatorios")
                return
            consulta_sql="INSERT INTO tipo (nome_tipo,publico,padrao_tamanho,sigla_tipo)VALUES(%s,%s,%s,%s)"
            parametros =(nome,publico,padraoGrade,siglaTipo)
            
            resultado = executar_sql(consulta_sql, parametros)

            if resultado is not None:
                self.ui.errorlabel.setText("Cadastro realizado com sucesso!")
                self.ui.nome.clear()
                self.ui.siglaTipo.clear()
                self.ui.padraoGrade.setCurrentIndex(0)
                self.ui.publico.setCurrentIndex(0)
                carregar_combo_boxes_tela(self.ui)
                carregar_todas_combo_box()
                
            else:
                self.ui.errorlabel.setText("Error ao realizar cadastro.Verifique os dados.")
        except   Exception as e:
            print(f'[ERRO] Erro no cadastro:{e}')
            self.ui.errorlabel.setText(f"Erro:{str(e)}")
        