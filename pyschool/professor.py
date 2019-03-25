from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto, materia):
        super().__init__(nome, nascimento, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto)
        self.__materia = materia
    
    def getMateria(self):
        return self.__materia
        
    def setMateria(self, materia):
        self.__materia = materia
    
    
    
    