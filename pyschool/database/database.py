import dataset

def criarBanco():
    db = dataset.connect('sqlite:///database/database.db')
    table = db.create_table('servidor')

def inserirServidor(servidor):
    db = dataset.connect('sqlite:///database/database.db')
    table = db.load_table('servidor')

    #data = dict(nome=servidor.getNome(), nascimento=servidor.getNascimento(), sexo=servidor.getSexo(),rg=servidor.getRg(),cpf=servidor.getCpf(),
    #            telefone=servidor.getTelefone(),rua=servidor.getRua(),bairro=servidor.getBairro(),numero=servidor.getNumero(),cep=servidor.getCep(),
    #            cidade=servidor.getCidade(),estado=servidor.getEstado(),email=servidor.getEmail(),senha=servidor.getSenha(),estadoCivil=servidor.getEstadoCivil(),
    #            foto=servidor.getFoto(),adm=servidor.getAdm(),cargo=servidor.getCargo())

    data = dict(nome=servidor.nome, nascimento=servidor.nascimento, sexo=servidor.sexo,rg=servidor.rg,cpf=servidor.cpf,
                telefone=servidor.telefone,rua=servidor.rua, bairro=servidor.bairro,numero=servidor.numero,cep=servidor.cep,
                cidade=servidor.cidade,estado=servidor.estado,email=servidor.email,senha=servidor.senha,estadoCivil=servidor.estadoCivil,
                foto=servidor.foto,adm=servidor.adm,cargo=servidor.cargo)

    table.insert(data)
