import os 
from PyQt5 import uic
from config.permissoes import TODAS_ACOES, PERMISSOES,TODOS_MENUS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class TelaPrincipal:
    def __init__(self, cargo):
        print(f"TelaPrincipal iniciada com cargo: {cargo}")
        self.ui = uic.loadUi(os.path.join(BASE_DIR, "resources", "principal", "main.ui"))
        self.cargo = cargo
        self.configurar_interface()

    def configurar_interface(self):
        permissoes = PERMISSOES.get(self.cargo, {"menus": [], "acoes": []})

        # Esconder todos os menus
        for menu_name in TODOS_MENUS:
            menu = getattr(self.ui, menu_name, None)
            if menu:
                menu.menuAction().setVisible(False)

        # Esconder todas ações
        for action_name in TODAS_ACOES:
            action = getattr(self.ui, action_name, None)
            if action:
                action.setVisible(False)

        # Mostrar menus permitidos
        for menu_name in permissoes["menus"]:
            menu = getattr(self.ui, menu_name, None)
            if menu:
                menu.menuAction().setVisible(True)

        # Mostrar ações permitidas
        for action_name in permissoes["acoes"]:
            action = getattr(self.ui, action_name, None)
            if action:
                action.setVisible(True)
        self.ui.actionCADASTRO.triggered.connect(self.abrir_tela_cadastro)
        self.ui.actionCADASTROPRODUTO.triggered.connect(self.abrir_tela_cadastroProduto)
    def abrir_tela_cadastro(self):
        from interfaces.cadastroFuncionario import TelaCadastroFuncionario
        self.tela_cadastro = TelaCadastroFuncionario()
    def abrir_tela_cadastroProduto(self):
        from interfaces.cadastroProduto import TelaCadastroProduto
        self.tela_cadastroProduto = TelaCadastroProduto()
        self.tela_cadastroProduto.ui.show()

    def show(self):
        self.ui.show()
    