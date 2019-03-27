# Classe Pessoa
class Pessoa:

    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, foto = None):
        #Mudar tudo pra não obrigatório ou pra set?
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.email = email
        self.senha = senha
        self.estadoCivil = estadoCivil
        self.foto = foto

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.capitalize()

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def estadoCivil(self):
        return self.__estadoCivil

    @estadoCivil.setter
    def estadoCivil(self, estadoCivil):
        self.__estadoCivil = estadoCivil

    @property
    def foto(self):
        return self.__foto

    @foto.setter
    def foto(self, foto):
        self.__foto = foto

    """
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

        def getFoto(self):
            return self.__foto

        def setFoto(self, foto):
            self.__foto = foto
    """