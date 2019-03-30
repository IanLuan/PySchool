from database import database

# Classe Pessoa
class Pessoa:

    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto = None):
        self.setNome(nome)
        self.setNascimento(nascimento)
        self.setSexo(sexo)
        self.setRg(rg)
        self.setCpf(cpf)
        self.setTelefone(telefone)
        self.setEndereco(endereco)
        self.setEmail(email)
        self.setSenha(senha)
        self.setEstadoCivil(estadoCivil)
        self.setFoto(foto)

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

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

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

    def getFoto(self):
        return self.__foto

    def setFoto(self, foto):
        self.__foto = foto

    def autenticar(self, nome, email):
        id, type = database.autenticar(nome, email)

        if id == None:
            raise UserWarning

        return id, type


