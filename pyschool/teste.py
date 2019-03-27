from pyschool.cargo import *
from pyschool.database import database

database.cr
cargo = Cargo("Secretário(a)")
database.inserirCargo(cargo)

cargo = Cargo("Diretor(a)")
database.inserirCargo(cargo)

cargo = Cargo("Coordenador(a)")
database.inserirCargo(cargo)



