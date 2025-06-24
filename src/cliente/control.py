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

    def atualizar_cliente(self, cpf, novos_dados):
        """
        Atualiza os dados de um cliente existente.
        :param cpf: str
        :param novos_dados: dict com os novos dados do cliente
        :return: Objeto ModeloCliente atualizado ou None
        """
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente:
            for chave, valor in novos_dados.items():
                setattr(cliente, chave, valor)
            return cliente
        return None

    def deletar_cliente(self, cpf):
        """
        Remove um cliente pelo CPF.
        :param cpf: str
        :return: True se o cliente foi removido, False caso contrário
        """
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente:
            self.clientes.remove(cliente)
            return True
        return False