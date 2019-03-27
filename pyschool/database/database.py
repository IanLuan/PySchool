import dataset

def criarBanco():
    db = dataset.connect('sqlite:///database/database.db')
    table = db.create_table('servidor')
    table = db.create_table('cargo')

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

def mostrarCargos():
    db = dataset.connect('sqlite:///database/database.db')
    cargos = []
    for x in db['cargo']:
        cargos.append(x['nome'])

    return cargos