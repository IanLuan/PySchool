import dataset
from pyschool.turma import turma

def inserirServidor(servidor):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['servidor']

    data = dict(nome=servidor.getNome(), nascimento=servidor.getNascimento(), sexo=servidor.getSexo(),rg=servidor.getRg(),cpf=servidor.getCpf(),
                telefone=servidor.getTelefone(),rua=servidor.getRua(),bairro=servidor.getBairro(),numero=servidor.getNumero(),cep=servidor.getCep(),
                cidade=servidor.getCidade(),estado=servidor.getEstado(),email=servidor.getEmail(),senha=servidor.getSenha(),estadoCivil=servidor.getEstadoCivil(),
                foto=servidor.getFoto(),adm=servidor.getAdm(),cargo=servidor.getCargo())
    table.insert(data)

def inserirCargo(cargo):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['cargo']

    data = dict(nome=cargo.getNome())
    table.insert(data)

def inserirTurma(turma):
    db = dataset.connect('sqlite:///database/database.db')
    table = db['turma']

    data = dict(serie=turma.getSerie(),grupo=turma.getGrupo(),maxAlunos=turma.getMaxAlunos(),status=turma.getStatus())
    table.insert(data)

def mostrarTurmasAtivas():
    db = dataset.connect('sqlite:///database/database.db')
    turmasAtivas = []
    for x in db['turma']:
        turmasAtivas.append(Turma(x['serie'], x['grupo'], x['maxAlunos'], x['status']))
    return turmasAtivas

def mostrarTurmas():

def mostrarCargos():
    db = dataset.connect('sqlite:///database/database.db')
    cargos = []
    for x in db['cargo']:
        cargos.append(x['nome'])
    return cargos