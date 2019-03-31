from database import database
class Cargo():

    def __init__(self, nome):
        self.setNome(nome)

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        if nome == "":
            raise ValueError
        elif database.existe(nome, "cargo"):
            raise Warning
        self.__nome = nome