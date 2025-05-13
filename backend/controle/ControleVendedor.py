class ControleVendedor:
    """
    Controla os dados do ModeloVendedor
    """

    def __init__(self, controle_dados):
        """
        Importa os dados do vendedor
        controle_dados: instancia de ControleDados
        """
        self.vendedores = controle_dados.get_vendedores()

    def listar_vendedores(self):
        """
        Lista todos os vendedores cadastrados.
        """
        return [str(vendedor) for vendedor in self.vendedores]

    def adicionar_vendedor(self, vendedor):
        """
        Adiciona um novo vendedor.
        :param vendedor: Objeto ModeloVendedor
        """
        self.vendedores.append(vendedor)

    def buscar_vendedor_por_id(self, id_vendedor):
        """
        Busca um vendedor pelo ID.
        :param id_vendedor: int
        :return: Objeto ModeloVendedor ou None
        """
        for vendedor in self.vendedores:
            if vendedor.id == id_vendedor:
                return vendedor
        return None