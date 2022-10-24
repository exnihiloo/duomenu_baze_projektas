from teatras_modelis import engine, Sale, Spektaklis, Rezisierius, Aktorius, Vaidmuo
from sqlalchemy.orm import sessionmaker


session = sessionmaker(bind=engine)()