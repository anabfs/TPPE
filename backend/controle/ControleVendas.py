class ControleVenda:
    """
    Controla os dados do ModeloVenda
    """

    def __init__(self, controle_dados):
        """
        Importa os dados da venda
        controle_dados: instancia de ControleDados
        """
        self.vendas = controle_dados.get_vendas()

    def listar_vendas(self):
        """
        Lista todas as vendas cadastradas.
        """
        return [str(venda) for venda in self.vendas]

    def adicionar_venda(self, venda):
        """
        Adiciona uma nova venda.
        :param venda: Objeto ModeloVenda
        """
        self.vendas.append(venda)

    def buscar_venda_por_id(self, id_venda):
        """
        Busca uma venda pelo ID.
        :param id_venda: int
        :return: Objeto ModeloVenda ou None
        """
        for venda in self.vendas:
            if venda.id == id_venda:
                return venda
        return None