import os

from sqlmodel import create_engine, Session, text

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
server = os.getenv("SERVER_NAME")
bdd = os.getenv("BDD_NAME")
port = os.getenv("PORT")

DATABASE_URL = (
                f"mssql+pyodbc://{username}:{password}@{server}:{port}/"
                f"{bdd}?driver=ODBC+Driver+18+for+SQL+Server&timeout=60"
)


def create_session(database_url=DATABASE_URL):
    engine = create_engine(DATABASE_URL)
    return Session(engine)





engine = create_engine(DATABASE_URL)

with Session(engine) as session:
    results = session.exec(text("SELECT TOP (10) * FROM [SalesLT].[Product]"))
    for thing in results:
        print(thing)