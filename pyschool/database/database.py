import dataset
from endereco import *
from professor import *

#PROFESSOR
def inserirProfessor(professor):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['professor']

    data = dict(nome=professor.getNome(), nascimento=professor.getNascimento(), sexo=professor.getSexo(),rg=professor.getRg(),cpf=professor.getCpf(),
                telefone=professor.getTelefone(), id_endereco = professor.getEndereco(), email=professor.getEmail(),senha=professor.getSenha(),estadoCivil=professor.getEstadoCivil(),
                foto=professor.getFoto())
    table.insert(data)

def mostrarDadosProfessor(id):
    db = dataset.connect('sqlite:///database/database.db')

    statement = "select professor.nome as nome, nascimento, sexo, rg, cpf, telefone, email, estadoCivil, foto, materia.nome as materia, rua," \
                " numero, bairro, cidade, estado, cep from professor, ensino, materia, endereco where professor.id = '{}' and ensino.id_professor='{}' " \
                "and materia.id = ensino.id_materia and professor.id_endereco = endereco.id".format(id,id)

    materias = []

    for row in db.query(statement):
        nome = row['nome']
        nascimento = row['nascimento']
        sexo = row['sexo']
        rg = row['rg']
        email = row['email']
        estadoCivil = row['estadoCivil']
        foto = row['foto']
        cpf = row['cpf']
        telefone = row['telefone']
        rua = row['rua']
        numero = row['numero']
        bairro = row['bairro']
        cidade = row['cidade']
        estado = row['estado']
        cep = row['cep']
        materias.append(row['materia'])

    endereco = Endereco(rua, bairro, numero, cep, cidade, estado)
    professor = Professor(nome, nascimento, sexo, rg, cpf, telefone, endereco, email, None, estadoCivil, foto, materias)

    return professor

#MATÉRIA
def retornarIdMateria(materia):
    db = dataset.connect('sqlite:///database/database.db')

    statement = "SELECT id FROM materia WHERE nome='{}'".format(materia)

    for row in db.query(statement):
        return row['id']

def inserirMateria(nome_materia):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['materia']

    data = dict(nome=nome_materia)
    table.insert(data)

def mostrarMaterias():
    db = dataset.connect('sqlite:///database/database.db')
    materias = []
    for x in db['materia']:
        materias.append(x['nome'])
    return materias

#ALUNO

#CARGO
def inserirCargo(nome_cargo):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['cargo']

    data = dict(nome=nome_cargo)
    table.insert(data)

def mostrarCargos():
    db = dataset.connect('sqlite:///database/database.db')
    cargos = []
    for x in db['cargo']:
        cargos.append(x['nome'])
    return cargos

#SERVIDOR
def inserirServidor(servidor):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['servidor']

    data = dict(nome=servidor.getNome(), nascimento=servidor.getNascimento(), sexo=servidor.getSexo(),rg=servidor.getRg(),cpf=servidor.getCpf(),
                telefone=servidor.getTelefone(), id_endereco = servidor.getEndereco(), email=servidor.getEmail(),senha=servidor.getSenha(),estadoCivil=servidor.getEstadoCivil(),
                foto=servidor.getFoto(),cargo=servidor.getCargo())
    table.insert(data)

#ADMINISTRADOR
def inserirAdministrador(administrador):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['administrador']

    data = dict(nome=administrador.getNome(), nascimento=administrador.getNascimento(), sexo=administrador.getSexo(),rg=administrador.getRg(),
                cpf=administrador.getCpf(), telefone=administrador.getTelefone(), id_endereco = administrador.getEndereco(), email=administrador.getEmail(),
                senha=administrador.getSenha(),estadoCivil=administrador.getEstadoCivil(),foto=administrador.getFoto(),cargo=administrador.getCargo())
    table.insert(data)

#TURMA
def inserirTurma(turma):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['turma']

    data = dict(serie=turma.getSerie(),grupo=turma.getGrupo(),maxAlunos=turma.getMaxAlunos(),status=turma.getStatus())
    table.insert(data)

def mostrarSeries():
    db = dataset.connect('sqlite:///database/database.db')
    table = db['turma']

    series = []
    for row in table.distinct('serie'):
        series.append(row['serie'])

    return series

def mostrarSeriesAtivas():
    db = dataset.connect('sqlite:///database/database.db')
    series = []

    statement = 'SELECT DISTINCT serie FROM turma where status=1'
    for row in db.query(statement):
        series.append(row['serie'])

    return series

def mostrarGruposAtivos(serie):
    db = dataset.connect('sqlite:///database/database.db')
    grupos = []

    statement = 'SELECT DISTINCT grupo FROM turma where serie="{}"'.format(serie) + ' and status=1'

    for row in db.query(statement):
        grupos.append(row['grupo'])

    return grupos

def mostrarQuantidadeMax(serie, grupo):
    db = dataset.connect('sqlite:///database/database.db')
    quantidade = 0

    statement = 'SELECT maxAlunos FROM turma where serie="{}"'.format(serie) + ' and status=1 and grupo="{}"'.format(grupo)

    for row in db.query(statement):
        quantidade = row['maxAlunis']

    return quantidade


#PESSOA
def autenticar(email, senha):
    db = dataset.connect('sqlite:///database/database.db')

    statement = "SELECT id FROM professor WHERE email='{}' and senha='{}'".format(email, senha)

    id = None
    type = None

    for row in db.query(statement):
        id = row['id']
        type = "professor"

    statement = "SELECT id FROM servidor WHERE email='{}' and senha='{}'".format(email, senha)

    for row in db.query(statement):
        id = row['id']
        type = "servidor"

    statement = "SELECT id FROM administrador WHERE email='{}' and senha='{}'".format(email, senha)

    for row in db.query(statement):
        id = row['id']

    return id, type


#CLASSE (Relação de professor e turma)
def inserirClasse(materias):
    db = dataset.connect('sqlite:///database/database.db')

    id_professores = []
    id_turma = retornarUltimoId("turma")

    for x in materias:
        mat_prof = x.split(" - ")
        professor = mat_prof[1]
        professor = professor.replace('Prof. ', '')

        statement = "SELECT id FROM professor WHERE nome = '{}'".format(professor)
        for row in db.query(statement):
            id_professores.append(row['id'])

    table = db['classe']

    for x in id_professores:
        data = dict(id_professor=x, id_turma=id_turma)
        table.insert(data)


#ENSINO (Relação de professor e matéria)
def inserirEnsino(id_professor, materias):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['ensino']

    for x in materias:
        data = dict(id_professor=id_professor, id_materia=retornarIdMateria(x))
        table.insert(data)

def mostrarMateriasProfessor():
    db = dataset.connect('sqlite:///database/database.db')
    materias = []

    statement = "select materia.nome as materia, professor.nome as professor from ensino, materia, professor where ensino.id_professor = professor.id and ensino.id_materia = materia.id order by materia.nome"

    for row in db.query(statement):
        materias.append((row['materia'],row['professor']))

    return materias


#ENDERECO
def inserirEndereco(endereco):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['endereco']

    data = dict(rua=endereco.getRua(),bairro=endereco.getBairro(),numero=endereco.getNumero(),cep=endereco.getCep(),cidade=endereco.getCidade(),
                estado=endereco.getEstado())
    table.insert(data)

#UTEIS
def retornarUltimoId(tabela):
    db = dataset.connect('sqlite:///database/database.db')

    statement = "SELECT * FROM {} WHERE id = (SELECT MAX(id) FROM {})".format(tabela,tabela)

    for row in db.query(statement):
        return row['id']

def existe(nome, table):
    db = dataset.connect('sqlite:///database/database.db')

    statement = 'SELECT id FROM {} where nome="{}"'.format(table, nome)
    existe = False

    for row in db.query(statement):
        existe = True

    return True






