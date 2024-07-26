import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname}"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"

# conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# depreciado - será removido em futuro release
#print(engine.table_names())

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())

with Session(engine) as session:
    juliana = User(
        name = 'Luis',
        fullname='Luis Fernando Beloti',
        address=[Address(email_address='luisfernandobeloti@gmail.com')]

    )
    sandy = User(
        name='Sandy',
        fullname='Sandy Cardoso',
        address=[Address(email_address='sandy@email.br'),
                 Address(email_address='sandy@email.org')]
    )
    patrick = User(
        name='Patrick',
        fullname='Patrick Cardoso'
    )

    # enviando para o BD(persistencia de dados)
    session.add_all([juliana,sandy,patrick])

    session.commit()

    stmt = select(User).where(User.name.in_(['Luis','Sandy']))
    print('Recuperando usuarios a partir de condição de filtragem')

    for user in session.scalars(stmt):
        print(user)

    stmt_address = select(Address).where(Address.user_id.in_([2]))
    print('\nRecuperando os endereçoes de email de Sandy ')
    for address in session.scalars(stmt_address):
        print(address)

order_stmt = select(User).order_by(User.fullname.desc())
print('\nRecuperando info de maneira ordenada')
for result in session.scalars(order_stmt):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print('\nExecutando statemente a partir da connection')
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print('\nTotal de instancias em User')
for result in session.scalars(stmt_count):
    print(result)


