import dataset
from endereco import *
from professor import *
from administrador import *
from servidor import *

class Database:

    def __init__(self):
        self.db = dataset.connect('sqlite:///database/database.db')
        self.table_professor = self.db['professor']
        self.table_materia = self.db['materia']
        self.table_aluno = self.db['aluno']
        self.table_servidor = self.db['servidor']
        self.table_administrador = self.db['administrador']
        self.table_cargo = self.db['cargo']
        self.table_endereco = self.db['endereco']
        self.table_turma = self.db['turma']
        self.table_classe = self.db['classe']
        self.table_ensino = self.db['ensino']

    #PROFESSOR
    def inserirProfessor(self, professor):
        data = dict(nome=professor.getNome(), nascimento=professor.getNascimento(), sexo=professor.getSexo(),rg=professor.getRg(),cpf=professor.getCpf(),
                    telefone=professor.getTelefone(), id_endereco = professor.getEndereco(), email=professor.getEmail(),senha=professor.getSenha(),estadoCivil=professor.getEstadoCivil(),
                    foto=professor.getFoto())
        self.table_professor.insert(data)

    def mostrarDadosProfessor(self, id):
        statement = "select professor.nome as nome, nascimento, sexo, rg, cpf, telefone, email, estadoCivil, foto, materia.nome as materia " \
                    "from professor, ensino, materia where professor.id = '{}' and ensino.id_professor='{}' " \
                    "and materia.id = ensino.id_materia".format(id,id)

        materias = []

        for row in self.db.query(statement):
            nome = row['nome']
            nascimento = row['nascimento']
            sexo = row['sexo']
            rg = row['rg']
            email = row['email']
            estadoCivil = row['estadoCivil']
            foto = row['foto']
            cpf = row['cpf']
            telefone = row['telefone']
            materias.append(row['materia'])

        professor = Professor(nome, nascimento, sexo, rg, cpf, telefone, self.mostrarEndereco(id, "professor"), email, None, estadoCivil, foto, materias)
        return professor

    def mostrarProfessores(self):
        professores = []
        for x in self.db['professor']:
            professores.append(x['nome'])
        return professores


    #MATÉRIA
    def retornarIdMateria(self, materia):
        statement = "SELECT id FROM materia WHERE nome='{}'".format(materia)

        for row in self.db.query(statement):
            return row['id']

    def inserirMateria(self, nome_materia):
        data = dict(nome=nome_materia)
        self.table_materia.insert(data)

    def mostrarMaterias(self):
        materias = []
        for x in self.db['materia']:
            materias.append(x['nome'])
        return materias

    #ALUNO
    def inserirAluno(self,aluno):
        data = dict(nome=aluno.getNome(), nascimento=aluno.getNascimento(), sexo=aluno.getSexo(),rg=aluno.getRg(),cpf=aluno.getCpf(),
                    telefone=aluno.getTelefone(), id_endereco = aluno.getEndereco(), email=aluno.getEmail(),estadoCivil=aluno.getEstadoCivil(),
                    foto=aluno.getFoto(), matricula=aluno.getMatricula(), matriculado=True, nomePai = aluno.getNomePai(), telefonePai=aluno.getTelefonePai(), cpfPai=aluno.getCpfPai(),
                    nomeMae=aluno.getNomeMae(), telefoneMae=aluno.getTelefoneMae(), cpfMae=aluno.getCpfMae(), idTurma = self.mostrarIdTurma(aluno.getSerie(), aluno.getGrupo()),
                    tipoSanguineo=aluno.getTipoSanguineo())
        self.table_aluno.insert(data)

    def mostrarTodosAlunos(self):
        alunos = []
        for x in self.db['aluno']:
            alunos.append(x['nome'])
        return alunos

    #CARGO
    def inserirCargo(self, nome_cargo):
        data = dict(nome=nome_cargo)
        self.table_cargo.insert(data)

    def mostrarCargos(self):
        cargos = []
        for x in self.db['cargo']:
            cargos.append(x['nome'])
        return cargos

    #SERVIDOR
    def inserirServidor(self,servidor):
        data = dict(nome=servidor.getNome(), nascimento=servidor.getNascimento(), sexo=servidor.getSexo(),rg=servidor.getRg(),cpf=servidor.getCpf(),
                    telefone=servidor.getTelefone(), id_endereco = servidor.getEndereco(), email=servidor.getEmail(),senha=servidor.getSenha(),estadoCivil=servidor.getEstadoCivil(),
                    foto=servidor.getFoto(),cargo=servidor.getCargo())
        self.table_servidor.insert(data)

    def mostrarDadosServidor(self, id):
        statement = "select servidor.nome as nome, nascimento, cargo, sexo, rg, cpf, telefone, email, estadoCivil, foto " \
                    "from servidor where servidor.id = '{}'".format(id)

        for row in self.db.query(statement):
            nome = row['nome']
            nascimento = row['nascimento']
            sexo = row['sexo']
            rg = row['rg']
            email = row['email']
            estadoCivil = row['estadoCivil']
            foto = row['foto']
            cpf = row['cpf']
            telefone = row['telefone']
            cargo = row['cargo']

        servidor = Servidor(nome, nascimento, sexo, rg, cpf, telefone, self.mostrarEndereco(id, "servidor"), email, None, estadoCivil, foto, cargo)
        return servidor


    def mostrarServidores(self):
        servidores = []
        for x in self.db['servidor']:
            servidores.append(x['nome'])
        return servidores


    #ADMINISTRADOR
    def inserirAdministrador(self, administrador):
        data = dict(nome=administrador.getNome(), nascimento=administrador.getNascimento(), sexo=administrador.getSexo(),rg=administrador.getRg(),
                    cpf=administrador.getCpf(), telefone=administrador.getTelefone(), id_endereco = administrador.getEndereco(), email=administrador.getEmail(),
                    senha=administrador.getSenha(),estadoCivil=administrador.getEstadoCivil(),foto=administrador.getFoto(),cargo=administrador.getCargo())
        self.table_administrador.insert(data)

    def updateAdministrador(self, id, administrador):
        data = dict(id= id, nome=administrador.getNome(), nascimento=administrador.getNascimento(),
                    sexo=administrador.getSexo(), rg=administrador.getRg(),
                    cpf=administrador.getCpf(), telefone=administrador.getTelefone(),
                    id_endereco=administrador.getEndereco(), email=administrador.getEmail(),
                    senha=administrador.getSenha(), estadoCivil=administrador.getEstadoCivil(),
                    foto=administrador.getFoto(), cargo=administrador.getCargo())
        self.table_administrador.update(data, ['id'])

    def mostrarDadosAdministrador(self, id):
        statement = "select administrador.nome as nome, nascimento, cargo, sexo, rg, cpf, telefone, email, senha, estadoCivil, foto " \
                    "from administrador where administrador.id = '{}'".format(id)

        for row in self.db.query(statement):
            nome = row['nome']
            nascimento = row['nascimento']
            sexo = row['sexo']
            rg = row['rg']
            email = row['email']
            senha = row['senha']
            estadoCivil = row['estadoCivil']
            foto = row['foto']
            cpf = row['cpf']
            telefone = row['telefone']
            cargo = row['cargo']

        administrador = Administrador(nome, nascimento, sexo, rg, cpf, telefone, self.mostrarEndereco(id, "administrador"), email,
                            senha, estadoCivil, foto, cargo)
        return administrador

    #TURMA
    def inserirTurma(self, turma):
        data = dict(serie=turma.getSerie(),grupo=turma.getGrupo(),maxAlunos=turma.getMaxAlunos(),status=turma.getStatus())
        self.table_turma.insert(data)

    def mostrarSeries(self):
        series = []
        for row in self.table_turma.distinct('serie'):
            series.append(row['serie'])

        return series

    def mostrarSeriesAtivas(self):
        series = []

        statement = 'SELECT DISTINCT serie FROM turma where status=1'
        for row in self.db.query(statement):
            series.append(row['serie'])
        return series

    def mostrarGruposAtivos(self, serie):
        grupos = []

        statement = 'SELECT DISTINCT grupo FROM turma where serie="{}"'.format(serie) + ' and status=1'

        for row in self.db.query(statement):
            grupos.append(row['grupo'])

        return grupos

    def mostrarQuantidadeMax(self, serie, grupo):
        quantidade = 0

        statement = 'SELECT maxAlunos FROM turma where serie="{}"'.format(serie) + ' and status=1 and grupo="{}"'.format(grupo)

        for row in self.db.query(statement):
            quantidade = row['maxAlunos']

        return quantidade

    def mostrarIdTurma(self, serie, grupo):
        id = ""
        statement = 'SELECT id FROM turma where serie="{}"'.format(
            serie) + ' and status=1 and grupo="{}"'.format(grupo)

        for row in self.db.query(statement):
            id = row['id']

        return id

    def mostrarTodasTurmas(self):
        turmas = []

        statement = "SELECT DISTINCT serie, grupo FROM turma where status = 1 order by serie"
        for row in self.db.query(statement):
            turmas.append(row['serie'] + " " +row['grupo'])
        return turmas

    #PESSOA
    def autenticar(self, email, senha):
        statement = "SELECT id FROM professor WHERE email='{}' and senha='{}'".format(email, senha)

        id = None
        type = None

        for row in self.db.query(statement):
            id = row['id']
            type = "professor"

        statement = "SELECT id FROM servidor WHERE email='{}' and senha='{}'".format(email, senha)

        for row in self.db.query(statement):
            id = row['id']
            type = "servidor"

        statement = "SELECT id FROM administrador WHERE email='{}' and senha='{}'".format(email, senha)

        for row in self.db.query(statement):
            id = row['id']
            type = "administrador"

        return id, type

    #CLASSE (Relação de professor e turma)
    def inserirClasse(self, materias):
        id_professores = []
        id_turma = self.retornarUltimoId("turma")

        for x in materias:
            mat_prof = x.split(" - ")
            professor = mat_prof[1]
            professor = professor.replace('Prof. ', '')

            statement = "SELECT id FROM professor WHERE nome = '{}'".format(professor)
            for row in self.db.query(statement):
                id_professores.append(row['id'])

        for x in id_professores:
            data = dict(id_professor=x, id_turma=id_turma)
            self.table_classe.insert(data)

    #ENSINO (Relação de professor e matéria)
    def inserirEnsino(self, id_professor, materias):
        for x in materias:
            data = dict(id_professor=id_professor, id_materia=self.retornarIdMateria(x))
            self.table_ensino.insert(data)

    def mostrarMateriasProfessor(self):
        materias = []

        statement = "select materia.nome as materia, professor.nome as professor from ensino, materia, professor where ensino.id_professor = professor.id and ensino.id_materia = materia.id order by materia.nome"

        for row in self.db.query(statement):
            materias.append((row['materia'],row['professor']))

        return materias

    #ENDERECO
    def inserirEndereco(self, endereco):
        data = dict(rua=endereco.getRua(),bairro=endereco.getBairro(),numero=endereco.getNumero(),cep=endereco.getCep(),cidade=endereco.getCidade(),
                    estado=endereco.getEstado())
        self.table_endereco.insert(data)

    def mostrarEndereco(self, id, table):
        statement = "select rua, numero, bairro, cidade, estado, cep from {}, endereco where {}.id = '{}' and {}.id_endereco = endereco.id".format(table, table, id, table)

        for row in self.db.query(statement):
            rua = row['rua']
            numero = row['numero']
            bairro = row['bairro']
            cidade = row['cidade']
            estado = row['estado']
            cep = row['cep']

        endereco = Endereco(rua, bairro, numero, cep, cidade, estado)
        return endereco

    def updateEndereco(self, endereco, id, table):

        id_endereco = self.retornarIdEndereco(id, table)
        data = dict(id=id_endereco, rua=endereco.getRua(),bairro=endereco.getBairro(),numero=endereco.getNumero(),cep=endereco.getCep(),cidade=endereco.getCidade(),
                    estado=endereco.getEstado())

        self.table_endereco.update(data, ['id'])

    def retornarIdEndereco(self, id, table):
        statement = "select distinct endereco.id from endereco, {} where {}.id = '{}' and {}.id_endereco = endereco.id".format(table, table, id, table)

        for row in self.db.query(statement):
            id_endereco = row['id']

        return id_endereco

    #UTEIS
    def retornarUltimoId(self, tabela):
        statement = "SELECT * FROM {} WHERE id = (SELECT MAX(id) FROM {})".format(tabela,tabela)

        for row in self.db.query(statement):
            return row['id']

    def existe(self, nome, table):
        statement = 'SELECT id FROM {} where nome="{}"'.format(table, nome)
        existe = False

        for row in self.db.query(statement):
            existe = True

        return existe