class ControleProduto:
    """
    Controla os dados do ModeloProduto
    """

    def __init__(self, controle_dados):
        """
        Importa os dados do produto
        controle_dados: instancia de ControleDados
        """
        self.produtos = controle_dados.get_produtos()

    def listar_produtos(self):
        """
        Lista todos os produtos cadastrados.
        """
        return [str(produto) for produto in self.produtos]

    def adicionar_produto(self, produto):
        """
        Adiciona um novo produto.
        :param produto: Objeto ModeloProduto
        """
        self.produtos.append(produto)

    def buscar_produto_por_id(self, id_produto):
        """
        Busca um produto pelo ID.
        :param id_produto: int
        :return: Objeto ModeloProduto ou None
        """
        for produto in self.produtos:
            if produto.id == id_produto:
                return produto
        return None