import dataset

#Inserção em ensino: matéria que relaciona professor e matéria

def autenticar(email,senha):
    db = dataset.connect('sqlite:///database/database.db')

    statement = "SELECT id FROM professor WHERE email='{}' and senha='{}'".format(email,senha)

    id = None
    type = None

    for row in db.query(statement):
        id = row['id']
        type = "professor"

    statement = "SELECT id FROM servidor WHERE email='{}' and senha='{}'".format(email, senha)

    for row in db.query(statement):
        id = row['id']
        type = "servidor"

   # statement = "SELECT id FROM administrador WHERE email='{}' and senha='{}'".format(email, senha)

   #for row in db.query(statement):
   #     id = row['id']

    return id, type

def inserirEnsino(id_professor, materias):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['ensino']

    for x in materias:
        data = dict(id_professor=id_professor, id_materia=retornarIdMateria(x))
        table.insert(data)

def inserirEndereco(endereco):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['endereco']

    data = dict(rua=endereco.getRua(),bairro=endereco.getBairro(),numero=endereco.getBairro(),cep=endereco.getCep(),cidade=endereco.getCidade(),
                estado=endereco.getEstado())
    table.insert(data)

def retornarUltimoId(tabela):
    db = dataset.connect('sqlite:///database/database.db')

    statement = "SELECT * FROM {} WHERE id = (SELECT MAX(id) FROM {})".format(tabela,tabela)

    for row in db.query(statement):
        return row['id']

def retornarIdMateria(materia):
    db = dataset.connect('sqlite:///database/database.db')

    statement = "SELECT id FROM materia WHERE nome='{}'".format(materia)

    for row in db.query(statement):
        return row['id']

def inserirServidor(servidor):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['servidor']

    data = dict(nome=servidor.getNome(), nascimento=servidor.getNascimento(), sexo=servidor.getSexo(),rg=servidor.getRg(),cpf=servidor.getCpf(),
                telefone=servidor.getTelefone(), id_endereco = servidor.getEndereco(), email=servidor.getEmail(),senha=servidor.getSenha(),estadoCivil=servidor.getEstadoCivil(),
                foto=servidor.getFoto(),adm=servidor.getAdm(),cargo=servidor.getCargo())
    table.insert(data)

def inserirProfessor(professor):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['professor']

    data = dict(nome=professor.getNome(), nascimento=professor.getNascimento(), sexo=professor.getSexo(),rg=professor.getRg(),cpf=professor.getCpf(),
                telefone=professor.getTelefone(), id_endereco = professor.getEndereco(), email=professor.getEmail(),senha=professor.getSenha(),estadoCivil=professor.getEstadoCivil(),
                foto=professor.getFoto())
    table.insert(data)

def inserirTurma(turma):
    db = dataset.connect('sqlite:////database/database.db')
    table = db['turma']

    data = dict(serie=turma.getSerie(),grupo=turma.getGrupo(),maxAlunos=turma.getMaxAlunos(),status=turma.getStatus())
    table.insert(data)

def mostrarSeries():
    db = dataset.connect('sqlite:///database/database.db')
    table = db['turma']

    series = []
    for row in table.distinct('serie'):
        series.append(row['nome'])

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

def inserirCargo(nome_cargo):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['cargo']

    data = dict(nome=nome_cargo)
    table.insert(data)

def mostrarCargos():
    db = dataset.connect('sqlite:///database/database.db')
    cargos = []
    for x in db['cargo']:
        print("a")
        cargos.append(x['nome'])
    return cargos

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