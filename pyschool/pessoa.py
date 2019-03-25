# Pessoa
class Pessoa:

    def __init__(self, nome, nascimento, rg, cpf, telefone, rua, bairro, numero, cep, cidade, estado, email, senha):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone
        self.__rua = rua
        self.__bairro = bairro
        self.__numero = numero
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado
        self.__email = email
        self.__senha = senha

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
