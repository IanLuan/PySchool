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
        if rua == "":
            raise ValueError
        self.__rua = rua

    def getBairro(self):
        return self.__bairro

    def setBairro(self, bairro):
        if bairro == "":
            raise ValueError
        self.__bairro = bairro

    def getNumero(self):
        return self.__numero

    def setNumero(self, num):
        if num == "":
            raise ValueError
        self.__numero = num

    def getCep(self):
        return self.__cep

    def setCep(self, cep):
        if cep == "":
            raise ValueError
        self.__cep = cep

    def getCidade(self):
        return self.__cidade

    def setCidade(self, cidade):
        if cidade == "":
            raise ValueError
        self.__cidade = cidade

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        if estado == "":
            raise ValueError
        self.__estado = estado