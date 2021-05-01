class ContaBancaria:

    def __init__(self, conta, saldo=5000):
        self.__saldo = float(saldo)
        self.conta = conta

    def consultar(self):
        return self.__saldo

    def adicionar(self,dinheiro):
        self.__saldo = self.__saldo + dinheiro

    def retirar(self, dinheiro):
        checagem = self.__checagem(dinheiro)

        if checagem:
            self.__saldo = self.__saldo - dinheiro
            return True
        else:
            return False

    def __checagem(self, dinheiro):
        if dinheiro > self.__saldo:
            return False
        else:
            return True