#from pyschool.pessoa import Pessoa
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto, matricula, matriculado, nomePai, telefonePai, cpfPai, nomeMae, telefoneMae, cpfMae, serie, turma, tipoSanguineo, observacao):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto)
        self.__matricula = self.setMatricula(matricula)
        self.__matriculado = self.setMatriculado(matriculado)
        self.__nomePai = self.setNomePai(nomePai)
        self.__telefonePai = self.setTelefonePai(telefonePai)
        self.__cpfPai = self.setCpfPai(cpfPai)
        self.__nomeMae = self.setNomeMae(nomeMae)
        self.__telefoneMae = self.setTelefoneMae(telefoneMae)
        self.__cpfMae = self.setCpfMae(cpfMae)
        self.__serie = self.setSerie(serie)
        self.__turma = self.setTurma(turma)
        self.__tipoSanguineo = self.setTipoSanguineo(tipoSanguineo)
        self.__observacao = self.setObservacao(observacao)

    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, matricula):
        self.__matricula = matricula
    
    def getMatriculado(self):
        return self.__matriculado
    
    def setMatriculado(self, matriculado):
        self.__matriculado = matriculado
    
    def getNomePai(self):
        return self.__nomePai
    
    def setNomePai(self, nomePai):
        self.__nomePai = nomePai

    def getTelefonePai(self):
        return self.__telefonePai

    def setTelefonePai(self, telefonePai):
        self.__telefonePai = telefonePai

    def getCpfPai(self):
        return self.__cpfPai

    def setCpfPai(self, cpfPai):
        self.__cpfPai = cpfPai

    def getNomeMae(self):
        return self.__nomeMae
    
    def setNomeMae(self, nomeMae):
        self.__nomeMae = nomeMae

    def getTelefoneMae(self):
        return self.__telefoneMae

    def setTelefoneMae(self, telefoneMae):
        self.__telefoneMae = telefoneMae

    def getCpfMae(self):
        return self.__cpfMae

    def setCpfMae(self, cpfMae):
        self.__cpfMae = cpfMae
    
    def getSerie(self):
        return self.__serie
    
    def setSerie(self, serie):
        self.__serie = serie
    
    def getTurma(self):
        return self.__turma
    
    def setTurma(self, turma):
        self.__turma = turma
    
    def getTipoSanguineo(self):
        return self.__tipoSanguineo
    
    def setTipoSanguineo(self, tipoSanguineo):
        self.__tipoSanguineo = tipoSanguineo
    
    def getObservacao(self):
        return self.__observacao
    
    def setObservacao(self, observacao):
        self.__observacao = observacao
    
    