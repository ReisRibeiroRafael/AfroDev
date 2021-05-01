class Restaurante:

    def __init__(self, nome, estrelas, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.cidade = cidade

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_estrelas(self, estrelas):
        self.estrelas = estrelas

    def get_estrelas(self):
        return self.estrelas

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_cidade(self):
        return self.cidade

    def jacquin(self):
        self.estrelas += 1