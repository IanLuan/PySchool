from pessoa import Pessoa
#from pyschool.pessoa import *

class Professor(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, foto, materia):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil,  foto)
        self.__materia = materia
    
    def getMateria(self):
        return self.__materia
        
    def setMateria(self, materia):
        self.__materia = materia
    
    
    
    