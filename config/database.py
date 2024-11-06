from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URI = "sqlite:///./DB.sqlite"

engine = create_engine(DATABASE_URI,connect_args={'check_same_thread':False})

Session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()