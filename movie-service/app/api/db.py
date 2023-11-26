
#sqlalchemy is the Python toolkit and Object Relational Mapper that gives application
#devlopers full power and flexibility of SQL
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
import os

#DATABASE_URL = 'postgresql://hajer:raHuvXtpahd7@localhost/movie_db'
DATABASE_URL = os.getenv('DATABASE_URL')
# l'object central de connectivité vers la base de données
engine = create_engine(DATABASE_URL)
#Un objet Metadata permet de collectionner plusieurs Tables de données
#sous forme de dictionnaire

metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts_id', ARRAY(String))
)

database = Database(DATABASE_URL)
