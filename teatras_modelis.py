from sqlalchemy import Column, Float, Integer, String, ForeignKey, Date, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///data/teatras.db')
Base = declarative_base()