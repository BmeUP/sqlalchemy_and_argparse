from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class First(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    second_name = Column(String)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.second_name)