class Cargo():

    def __init__(self, nome):
        self.setNome(nome)

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome