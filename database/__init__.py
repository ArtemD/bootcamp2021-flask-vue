from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']
db = create_engine(DATABASE_URL)