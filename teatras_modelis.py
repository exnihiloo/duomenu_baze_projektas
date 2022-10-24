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

class Spektaklis(Base):
    __tablename__ = 'spektaklis'
    id = Column(Integer, primary_key = True)
    pavadinimas = Column('pavadinimas', String)
    # premjera = Column('premjera', Date)
    sale_id = Column(Integer, ForeignKey('sale.id'))
    sale = relationship("Sale", back_populates = 'spektakliai')
    rezisierius_id = Column(Integer, ForeignKey('rezisierius.id'))
    rezisierius = relationship("Rezisierius", back_populates = 'spektakliai')


    def __repr__(self):
        return f"{self.id}) {self.pavadinimas}, salė: {self.sale}, režisierius {self.rezisierius}."


class Rezisierius(Base):
    __tablename__ = 'rezisierius'
    id = Column(Integer, primary_key = True)
    vardas = Column('vardas', String)
    pavarde = Column('pavarde', String)
    spektakliai = relationship('Spektaklis', back_populates = 'rezisierius')



    def __repr__(self):
        return f"{self.id}) {self.vardas} {self.pavarde}"