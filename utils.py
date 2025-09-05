from database import executar_sql

# Mapeamento de comboboxes por tela
mapa_combo_por_tela = {
    'TelaCadastroProduto': {
        'colecao': ('colecao', 'nome_colecao', 'id_colecao'),
        'modelo': ('modelo', 'nome_modelo', 'id_modelo'),
        'variacao': ('variacao', 'nome_variacao', 'id_variacao')
    },
    'TelaCadastroModelo': {
        'tipoPeca': ('tipo', 'nome_tipo', 'id_tipo')
    }
}

def carregar_combo_boxes_tela(ui, nome_tela):
    if nome_tela not in mapa_combo_por_tela:
        print(f"[AVISO] Nenhum combo box configurado para: {nome_tela}")
        return

    for nome_combo, (tabela, campo, campo_id) in mapa_combo_por_tela[nome_tela].items():
        combo_box = getattr(ui, nome_combo, None)
        if combo_box is not None:
            combo_box.clear()
            try:
                resultado = executar_sql(f"SELECT {campo_id}, {campo} FROM {tabela}")
                if resultado:
                    for id_item, nome_item in resultado:
                        combo_box.addItem(str(nome_item), id_item)
            except Exception as e:
                print(f"[ERRO] Erro ao carregar combo '{nome_combo}' da tela '{nome_tela}': {e}")
        else:
            print(f"[ERRO] Combo box '{nome_combo}' não encontrado na interface da tela '{nome_tela}'")

def carregar_todas_combo_box(tela_produto=None, tela_modelo=None):
    if tela_produto:
        carregar_combo_boxes_tela(tela_produto.ui, 'TelaCadastroProduto')
    if tela_modelo:
        carregar_combo_boxes_tela(tela_modelo.ui, 'TelaCadastroModelo')