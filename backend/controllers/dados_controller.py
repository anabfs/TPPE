from models.ModeloDados import ModeloDados

class ControleDados:
    """
    Controla os dados do ModeloDados
    """

    def __init__(self):
        self.d = ModeloDados()

    # -------------Gets e Sets ---------------------

    def get_modelo_dados(self):
        return self.d

    def set_modelo_dados(self, d):
        self.d = d

    def get_clientes(self):
        return self.d.get_clientes()

    def get_vendedores(self):
        return self.d.get_vendedores()

    def get_produtos(self):
        return self.d.get_produtos()

    def get_vendas(self):
        return self.d.get_vendas()

    def get_itens_venda(self):
        return self.d.get_itens_venda()