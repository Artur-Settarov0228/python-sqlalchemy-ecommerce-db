from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from .config import settengs


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",

    host= settengs.DB_HOST,
    port=settengs.DB_PORT,
    username=settengs.DB_USER,
    password=settengs.DB_PASS,
    database=settengs.DB_NAME
)

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)