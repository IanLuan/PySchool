from pessoa import Pessoa
#from pyschool.pessoa import *

class Professor(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto, materia):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil,  foto)
        self.__materia = materia
    
    def getMateria(self):
        return self.__materia
        
    def setMateria(self, materia):
        if materia == "":
            raise ValueError
        self.__materia = materia
    
    
    
    