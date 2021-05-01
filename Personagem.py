class Personagem:

    def __init__(self, nome, carro, forca, habilidade, vida):

        self.__nome = nome
        self. __carro = carro
        self. __forca = forca
        self. __habilidade = habilidade
        self. __vida = vida

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def atacar(self):
        if not self.__habilidade or self.__vida == 0:
            return 0
        else:
            return self.__forca

    def defender(self, dano):
        if not self.__habilidade:
            return self.__sofrer_dano(dano)
        elif dano > self.__forca:
            dano = dano - self.__forca
            return self.__sofrer_dano(dano)
        else:
            return self.__sofrer_dano(0)

    def __sofrer_dano(self, dano):
        if dano < self.__vida:
            self.__vida = self.__vida - dano
        else:
            self.__vida = 0
