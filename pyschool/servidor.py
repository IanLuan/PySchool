from pessoa import Pessoa

class servidor(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto, adm, cargo):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto)
        self.__adm = adm
        self.__cargo = cargo
    
    def getAdm(self):
        return self.__adm
    
    def setAdm(self, adm):
        self.__adm = adm

    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    