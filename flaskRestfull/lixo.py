from sqlalchemy.orm import sessionmaker
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db', convert_unicode=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
# Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
session.commit()


# our_user = session.query(User).filter_by(name='ed').first()
# print(our_user)