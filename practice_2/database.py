from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_url = "sqlite:///./canteen.db"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

localSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()