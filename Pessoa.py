class Pessoa:

    def __init__(self, altura, idade, cidade):
        self.altura = altura
        self.idade = idade
        self.cidade = cidade

    def set_altura(self,altura):
        self.altura = altura

    def get_altura(self):
        return self.altura

    def set_idade(self,idade):
        self.idade = idade

    def get_idade(self):
        return self.idade

    def set_cidade(self,cidade):
        self.cidade = cidade

    def get_cidade(self):
        return self.cidade

    def aniversario(self):
        self.idade += 1