class ControleCliente:
    """
    Controla os dados do ModeloCliente
    """

    def __init__(self, controle_dados):
        """
        Importa os dados do cliente
        controle_dados: instancia de ControleDados
        """
        self.clientes = controle_dados.get_clientes()

    def listar_clientes(self):
        """
        Lista todos os clientes cadastrados.
        """
        return [str(cliente) for cliente in self.clientes]

    def adicionar_cliente(self, cliente):
        """
        Adiciona um novo cliente.
        :param cliente: Objeto ModeloCliente
        """
        self.clientes.append(cliente)

    def buscar_cliente_por_cpf(self, cpf):
        """
        Busca um cliente pelo CPF.
        :param cpf: str
        :return: Objeto ModeloCliente ou None
        """
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None