#from pyschool.pessoa import Pessoa
from pessoa import Pessoa
#from pyschool.database import database
from database import database


class Servidor(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, foto, adm, cargo):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, foto)
        self.adm = adm
        self.cargo = cargo

    @property
    def adm(self):
        return self.__adm

    @adm.setter
    def adm(self, adm):
        self.__adm = adm

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    
    