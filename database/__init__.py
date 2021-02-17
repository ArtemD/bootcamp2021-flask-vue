from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()

class License(Base):
    __tablename__ = 'licenses'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    postcode = Column(String(255))
    city = Column(String(255))
    license_granting_date = Column(String(255))
    license_type = Column(String(255))
    business_id = Column(String(255))
    created_at  = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<License (name='%s', created_at='%s')>" % (self.name, self.created_at)

DATABASE_URL = os.environ['DATABASE_URL']
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)