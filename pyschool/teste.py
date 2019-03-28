from pyschool.database import database
import dataset

db = dataset.connect('sqlite:///database/database.db')
table = db['servidor']

var = "Mayara"

statement = "SELECT * FROM servidor WHERE id = (SELECT MAX( _id ) FROM servidor)"

for row in db.query(statement):
    print(row)