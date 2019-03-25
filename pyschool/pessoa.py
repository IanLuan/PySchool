# Classe Pessoa
class Pessoa:

    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa = None, foto = None):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__sexo = sexo
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone
        self.__rua = rua
        self.__bairro = bairro
        self.__numero = numero
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado
        self.__email = email
        self.__senha = senha
        self.__estadoCivil = estadoCivil
        self.__idPessoa = idPessoa
        self.__foto = foto

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getNascimento(self):
        return self.__nascimento

    def setNascimento(self, nascimento):
        self.__nascimento = nascimento

    def getSexo(self):
        return self.__sexo

    def setSexo(self, sexo):
        self.__sexo = sexo

    def getRg(self):
        return self.__rg

    def setRg(self, rg):
        self.__rg = rg

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def getRua(self):
        return self.__rua

    def setRua(self, rua):
        self.__rua = rua

    def getBairro(self):
        return self.__bairro

    def setBairro(self, bairro):
        self.__bairro = bairro

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = numero

    def getCep(self):
        return self.__cep

    def setCep(self, cep):
        self.__cep = cep

    def getCidade(self):
        return self.__cidade

    def setCidade(self, cidade):
        self.__cidade = cidade

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        self.__senha = senha

    def getEstadoCivil(self):
        return self.__estadoCivil

    def setEstadoCivil(self, estadoCivil):
        self.__estadoCivil = estadoCivil

    def getIdPessoa(self):
        return self.__idPessoa

    def setId(self, idPessoa):
        self.__idPessoa = idPessoa

    def getFoto(self):
        return self.__foto

    def setFoto(self, foto):
        self.__foto = foto