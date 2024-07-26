from msilib import Table

from sqlalchemy import create_engine, MetaData, Column, Integer, String

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData(schema='teste')

user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('email_adress', String(60)),
    Column('nickname', String(50), nullable=False)
)
