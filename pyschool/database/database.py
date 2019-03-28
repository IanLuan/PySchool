import dataset

def inserirEndereco(endereco):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['endereco']

    data = dict(rua=endereco.getRua(),bairro=endereco.getBairro(),numero=endereco.getBairro(),cep=endereco.getCep(),cidade=endereco.getCidade(),
                estado=endereco.getEstado())
    table.insert(data)

def retornarIdEndereco():
    db = dataset.connect('sqlite:///database/database.db')

    statement = "SELECT * FROM endereco WHERE id = (SELECT MAX(id) FROM endereco)"

    for row in db.query(statement):
        return row['id']

def inserirServidor(servidor):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['servidor']

    data = dict(nome=servidor.getNome(), nascimento=servidor.getNascimento(), sexo=servidor.getSexo(),rg=servidor.getRg(),cpf=servidor.getCpf(),
                telefone=servidor.getTelefone(), id_endereco = servidor.getEndereco(), email=servidor.getEmail(),senha=servidor.getSenha(),estadoCivil=servidor.getEstadoCivil(),
                foto=servidor.getFoto(),adm=servidor.getAdm(),cargo=servidor.getCargo())
    table.insert(data)

def inserirCargo(cargo):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['cargo']

    data = dict(nome=cargo.getNome())
    table.insert(data)

def inserirTurma(turma):
    db = dataset.connect('sqlite:///database.db')
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

def mostrarCargos():
    db = dataset.connect('sqlite:///database/database.db')
    cargos = []
    for x in db['cargo']:
        cargos.append(x['nome'])
    return cargos