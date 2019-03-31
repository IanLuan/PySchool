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
        if nome == "":
            raise ValueError
        self.__nome = nome

    def getNascimento(self):
        return self.__nascimento

    def setNascimento(self, nascimento):
        if nascimento == "":
            raise ValueError
        self.__nascimento = nascimento

    def getSexo(self):
        return self.__sexo

    def setSexo(self, sexo):
        if sexo == "":
            raise ValueError
        self.__sexo = sexo

    def getRg(self):
        return self.__rg

    def setRg(self, rg):
        if rg == "":
            raise ValueError
        self.__rg = rg

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        if cpf == "":
            raise ValueError
        self.__cpf = cpf

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        if telefone == "":
            raise ValueError
        self.__telefone = telefone

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        if endereco == "":
            raise ValueError
        self.__endereco = endereco

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        if email == "":
            raise ValueError
        self.__email = email

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        if senha == "":
            raise ValueError
        self.__senha = senha

    def getEstadoCivil(self):
        return self.__estadoCivil

    def setEstadoCivil(self, estadoCivil):
        if estadoCivil == "":
            raise ValueError
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


