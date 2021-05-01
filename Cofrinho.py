class Cofrinho:

    def __init__(self, peso, saldo):
        self.__saldo = saldo
        self.peso = peso

    def adicionar(self, dinheiro):
        self.__saldo = float(self.__saldo) + dinheiro

    def pesar(self):
        self.__peso()
        return self.peso

    def __peso(self):
        self.peso = self.__saldo * 10

    def quebrar_cofrinho(self):
        return self.__saldo
