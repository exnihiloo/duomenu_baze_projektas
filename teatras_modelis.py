from sqlalchemy import Column, Float, Integer, String, ForeignKey, Date, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///data/teatras.db')
Base = declarative_base()


association_table = Table('aktorius_spektaklis', Base.metadata,
    Column('spektaklis_id', Integer, ForeignKey('spektaklis.id')),
    Column('aktorius_id', Integer, ForeignKey('aktorius.id'))
)

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
    sale_id = Column(Integer, ForeignKey('sale.id'))
    sale = relationship("Sale", back_populates = 'spektakliai')
    rezisierius_id = Column(Integer, ForeignKey('rezisierius.id'))
    rezisierius = relationship("Rezisierius", back_populates = 'spektakliai')
    aktoriai = relationship("Aktorius", secondary = association_table, back_populates = 'spektakliai')
    vaidmenys = relationship("Vaidmuo", back_populates = 'spektaklis')

    def __repr__(self):
        return f"{self.id}) {self.pavadinimas}, salė: {self.sale}, režisierius {self.rezisierius}."


class Rezisierius(Base):
    __tablename__ = 'rezisierius'
    id = Column(Integer, primary_key = True)
    vardas = Column('vardas', String)
    pavarde = Column('pavarde', String)
    spektakliai = relationship('Spektaklis', back_populates = 'rezisierius')
    gimimo_data = Column("Gimimo data", Date)



    def __repr__(self):
        return f"{self.id}) {self.vardas} {self.pavarde} : {self.gimimo_data}"


class Aktorius(Base):
    __tablename__ = 'aktorius'
    id = Column(Integer, primary_key = True)
    vardas = Column('vardas', String)
    pavarde = Column('pavarde', String)
    gimimo_data = Column("Gimimo data", Date)
    spektakliai = relationship("Spektaklis", secondary = association_table, back_populates = 'aktoriai')
    vaidmenys = relationship("Vaidmuo", back_populates = 'aktoriai')

    def __repr__(self):
        return f"{self.id}) {self.vardas} {self.pavarde} : {self.gimimo_data}"


class Vaidmuo(Base):
    __tablename__ = 'vaidmuo'
    id = Column(Integer, primary_key = True)
    vaidmuo = Column("vaidmuo", String)
    aktorius_id = Column(Integer, ForeignKey("aktorius.id"))
    aktoriai = relationship("Aktorius", back_populates = 'vaidmenys')
    spektaklis_id = Column(Integer, ForeignKey("spektaklis.id"))
    spektaklis = relationship("Spektaklis", back_populates = 'vaidmenys')

    def __repr__(self):
        return f"{self.id}) {self.vaidmuo}, atliekamas aktoriaus/ės {self.aktoriai}, spektaklyje {self.spektaklis}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)