from sqlalchemy import Column, Float, Integer, String, ForeignKey, Date, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///data/teatras.db')
Base = declarative_base()



class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key = True)
    pavadinimas = Column('Sales pavadinimas', String)
    spektakliai = relationship("Spektaklis", back_populates = 'sale')


    def __repr__(self):
        return f"{self.id}) {self.pavadinimas}."