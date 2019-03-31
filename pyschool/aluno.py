#from pyschool.pessoa import Pessoa
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto, matricula, matriculado, nomePai, telefonePai, cpfPai, nomeMae, telefoneMae, cpfMae, serie, turma, tipoSanguineo, observacao):
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
        self.setTurma(turma)
        self.setTipoSanguineo(tipoSanguineo)
        self.setObservacao(observacao)

    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, matricula):
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
    
    def getTurma(self):
        return self.__turma
    
    def setTurma(self, turma):
        if turma == "":
            raise ValueError
        self.__turma = turma
    
    def getTipoSanguineo(self):
        return self.__tipoSanguineo
    
    def setTipoSanguineo(self, tipoSanguineo):
        if tipoSanguineo == "":
            raise ValueError
        self.__tipoSanguineo = tipoSanguineo
    
    def getObservacao(self):
        return self.__observacao
    
    def setObservacao(self, observacao):
        if observacao == "":
            raise ValueError
        self.__observacao = observacao
    
    