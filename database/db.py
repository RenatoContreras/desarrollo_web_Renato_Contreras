import pymysql
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



#Para el acceso a la base de datos utilice las siguientes 
#credenciales: host: localhost,
#puerto: 3306, 
# nombre base datos: tarea2, username: cc5002 y password:
#programacionweb


DB_NAME = 'tarea2'
DB_USERNAME = 'cc5002'
DB_PASSWORD = 'programacionweb'
DB_HOST = 'localhost'
DB_PORT = '3306'

DATABASE_URL = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


engine = create_engine(DATABASE_URL, echo = False, future = True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


#----------------------- funciones -----------------------


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





