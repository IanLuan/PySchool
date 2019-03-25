from pessoa import Pessoa

class servidor(Pessoa):
    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto, cargo):
        super().__init__(nome, nascimento, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha, estadoCivil, idPessoa, foto)
        seff.__cargo = cargo
    
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    