class Carro:
    __velocidade = 0

    def __init__(self, modelo, cor, motor):
        self.__modelo = modelo
        self.cor = cor
        self.motor = motor

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def acelerar(self):
        self.__velocidade += 1

    def get_velocidade(self):
        return self.__velocidade