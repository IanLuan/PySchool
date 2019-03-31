#from pyschool.pessoa import Pessoa
from pessoa import Pessoa
#from pyschool.database import database
from database import database

class Servidor(Pessoa):
   def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto, cargo):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto)
        self.__cargo = cargo

   def getCargo(self):
       return self.__cargo

   def setCargo(self, cargo):
       if cargo == "":
           raise ValueError
       self.__cargo = cargo


    
    