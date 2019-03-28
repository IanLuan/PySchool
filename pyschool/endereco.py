class Endereco():

    def __init__(self, rua, bairro, numero, cep, cidade, estado):
        self.setRua(rua)
        self.setBairro(bairro)
        self.setNumero(numero)
        self.setCep(cep)
        self.setCidade(cidade)
        self.setEstado(estado)

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

    def setNumero(self, num):
        self.__numero = num

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