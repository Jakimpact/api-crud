import os

from sqlmodel import create_engine, Session

username = os.getenv("USER")
password = os.getenv("PASSWORD")
server = os.getenv("SERVER_NAME")
bdd = os.getenv("BDD_NAME")
port = os.getenv("PORT")

DATABASE_URL = (
                f"mssql+pyodbc://{username}:{password}@{server}:{port}/"
                f"{bdd}?driver=ODBC+Driver+18+for+SQL+Server&timeout=60"
)

ENGINE = create_engine(DATABASE_URL)


def get_session():
    try:
        with Session(ENGINE) as session:
            yield session
    except:
        raise  
    finally:
        pass