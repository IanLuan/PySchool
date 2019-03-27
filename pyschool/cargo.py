class Cargo():

    def __init__(self, nome, id = None):
        self.__nome = nome
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id