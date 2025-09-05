import os
from PyQt5 import uic

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TODOS_MENUS = ["menuUSUARIOS", "menuPRODUTOS", "menuCLIENTES", "menuCOMPRAS"]

TODAS_ACOES = [
    "actionCADASTRO", "actionCONSULTAR", "actionINSERIR", "actionRETIRAR",
    "actionCADASTRO_2", "actionDESCONTOS",
    "actionDIARIAS", "actionMENSAL", "actionANUAL",
    "actionCADASTROPRODUTO",
]

PERMISSOES = {
    "Gerente": {
        "menus": TODOS_MENUS,
        "acoes": TODAS_ACOES,
    },
    "Caixa": {
        "menus": ["menuCOMPRAS"],
        "acoes": ["actionDIARIAS", "actionMENSAL", "actionANUAL"],
    },
    "Estoquista": {
        "menus": ["menuPRODUTOS"],
        "acoes": ["actionCONSULTAR", "actionINSERIR", "actionRETIRAR", "actionCADASTROPRODUTO"],
    },
    "Vendedor": {
        "menus": ["menuCLIENTES", "menuCOMPRAS"],
        "acoes": ["actionCADASTRO_2", "actionDESCONTOS", "actionDIARIAS"],
    },
}