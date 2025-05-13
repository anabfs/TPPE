import re

class Validador:
    """
    Classe para validação de dados como email e telefone.
    """

    def valida_email(self, email):
        """
        Verifica se o email informado é válido.
        email: string do email
        return: True se for válido, False caso contrário
        """
        if not email or email.startswith("@") or "@" not in email:
            return False
        return True

    def valida_telefone(self, telefone):
        """
        Verifica se o telefone informado está no formato certo.
        telefone: string do telefone
        return: True se for válido, False caso contrário
        """
        if len(telefone) != 11:
            return False
        if len(re.sub(r"\D", "", telefone)) != 11:
            return False
        if telefone in [
            "00000000000", "11111111111", "22222222222", "33333333333",
            "44444444444", "55555555555", "66666666666", "77777777777",
            "88888888888", "99999999999"
        ]:
            return False
        return True