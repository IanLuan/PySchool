#from pyschool.pessoa import Pessoa
from pessoa import Pessoa
#from pyschool.database import database
from database import database

class Servidor(Pessoa):
   def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, foto, adm, cargo):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, foto)
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


    
    