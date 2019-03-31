from servidor import Servidor

class Administrador(Servidor):

    def __init__(self, nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto, adm,
                 cargo):
        super().__init__(nome, nascimento, sexo, rg, cpf, telefone, endereco, email, senha, estadoCivil, foto, adm, cargo)