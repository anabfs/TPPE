class ModeloDados:
    """
    Classe que define os atributos e métodos do objeto.
    """

    def __init__(self):
        # -------------Atributos da classe----------------
        self.clientes = []
        self.vendedores = []
        self.produtos = []
        self.vendas = []
        self.itens_venda = []

    # -------------Gets e Sets ---------------------

    def get_clientes(self):
        return self.clientes

    def set_clientes(self, clientes):
        self.clientes = clientes

    def get_vendedores(self):
        return self.vendedores

    def set_vendedores(self, vendedores):
        self.vendedores = vendedores

    def get_produtos(self):
        return self.produtos

    def set_produtos(self, produtos):
        self.produtos = produtos

    def get_vendas(self):
        return self.vendas

    def set_vendas(self, vendas):
        self.vendas = vendas

    def get_itens_venda(self):
        return self.itens_venda

    def set_itens_venda(self, itens_venda):
        self.itens_venda = itens_venda