from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, materia):
        super().__init__()
        self.__materia = materia