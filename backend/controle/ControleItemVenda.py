class ControleItemVenda:
    """
    Controla os dados do ModeloItemVenda
    """

    def __init__(self, controle_dados):
        """
        Importa os dados dos itens de venda
        controle_dados: instancia de ControleDados
        """
        self.itens_venda = controle_dados.get_itens_venda()

    def listar_itens_venda(self):
        """
        Lista todos os itens de venda cadastrados.
        """
        return [str(item) for item in self.itens_venda]

    def adicionar_item_venda(self, item_venda):
        """
        Adiciona um novo item de venda.
        :param item_venda: Objeto ModeloItemVenda
        """
        self.itens_venda.append(item_venda)

    def buscar_item_por_id(self, id_item):
        """
        Busca um item de venda pelo ID.
        :param id_item: int
        :return: Objeto ModeloItemVenda ou None
        """
        for item in self.itens_venda:
            if item.id == id_item:
                return item
        return None