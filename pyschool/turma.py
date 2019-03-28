class Turma:
    def __init__(self, serie, grupo, maxAlunos, status=False):
        self.__serie = serie
        self.__grupo = grupo
        self.__maxAlunos = maxAlunos
        self.__status = status
    
    def getSerie(self):
        return self.__serie
    
    def setSerie(self, serie):
        self.__serie = serie
    
    def getGrupo(self):
        return self.__grupo
    
    def setGrupo(self, grupo):
        self.__grupo = grupo
    
    def getMaxAlunos(self):
        return self.__maxAlunos
    
    def setMaxAlunos(self, maxAlunos):
        self.__maxAlunos = maxAlunos

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status