from pessoa import Pessoa   

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto, matricula, matriculado, nomePai, nomeMae, serie, turma, tipoSanguineo, observacao):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto)
        self.__matricula = matricula
        self.__matriculado = matriculado
        self.__nomePai = nomePai
        self.__nomeMae = nomeMae
        self.__serie = serie
        self.__turma = turma
        self,__tipoSanguineo = tipoSanguineo
        self.__observacao = observacao

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
    
    def getNomeMae(self):
        return self.__nomeMae
    
    def setNomeMae(self, nomeMae):
        self.__nomeMae = nomeMae
    
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
    
    