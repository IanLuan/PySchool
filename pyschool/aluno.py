from pessoa import Pessoa
from datetime import datetime
from database.database import Database

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto, matricula, matriculado, nomePai, telefonePai, cpfPai, nomeMae, telefoneMae, cpfMae, serie, tipoSanguineo,  grupo):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto)
        self.setMatricula(matricula)
        self.setMatriculado(matriculado)
        self.setNomePai(nomePai)
        self.setTelefonePai(telefonePai)
        self.setCpfPai(cpfPai)
        self.setNomeMae(nomeMae)
        self.setTelefoneMae(telefoneMae)
        self.setCpfMae(cpfMae)
        self.setSerie(serie)
        self.setTipoSanguineo(tipoSanguineo)
        self.setGrupo(grupo)

    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, matricula):
        matricula = self.gerarMatricula()
        if matricula == "":
            raise ValueError
        self.__matricula = matricula
    
    def getMatriculado(self):
        return self.__matriculado
    
    def setMatriculado(self, matriculado):
        if matriculado == "":
            raise ValueError
        self.__matriculado = matriculado
    
    def getNomePai(self):
        return self.__nomePai
    
    def setNomePai(self, nomePai):
        if nomePai == "":
            raise ValueError
        self.__nomePai = nomePai

    def getTelefonePai(self):
        return self.__telefonePai

    def setTelefonePai(self, telefonePai):
        if telefonePai == "":
            raise ValueError
        self.__telefonePai = telefonePai

    def getCpfPai(self):
        return self.__cpfPai

    def setCpfPai(self, cpfPai):
        if cpfPai == "":
            raise ValueError
        self.__cpfPai = cpfPai

    def getNomeMae(self):
        return self.__nomeMae
    
    def setNomeMae(self, nomeMae):
        if nomeMae == "":
            raise ValueError
        self.__nomeMae = nomeMae

    def getTelefoneMae(self):
        return self.__telefoneMae

    def setTelefoneMae(self, telefoneMae):
        if telefoneMae == "":
            raise ValueError
        self.__telefoneMae = telefoneMae

    def getCpfMae(self):
        return self.__cpfMae

    def setCpfMae(self, cpfMae):
        if cpfMae == "":
            raise ValueError
        self.__cpfMae = cpfMae
    
    def getSerie(self):
        return self.__serie
    
    def setSerie(self, serie):
        if serie == "":
            raise ValueError
        self.__serie = serie
    
    def getGrupo(self):
        return self.__grupo
    
    def setGrupo(self, grupo):
        self.__grupo = grupo
    
    def getTipoSanguineo(self):
        return self.__tipoSanguineo
    
    def setTipoSanguineo(self, tipoSanguineo):
        if tipoSanguineo == "":
            raise ValueError
        self.__tipoSanguineo = tipoSanguineo

    def gerarMatricula(self):
        now = datetime.now()
        database = Database()
        print(now.year)
        print(database.retornarUltimoId("aluno"))
        matricula = str(now.year) + str(int(database.retornarUltimoId("aluno")) + 1)
        print(matricula)
        return matricula
