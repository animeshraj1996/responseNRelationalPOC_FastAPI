import sqlalchemy
from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session


def get_engine():
    connection_url = sqlalchemy.engine.URL.create(
        "mssql+pyodbc",
        username="sa",
        password="Root@123",
        host="TIGER01659\SQLEXPRESS2019",
        database="demo_foreign_key",
        query={
            "driver": "ODBC Driver 17 for SQL Server",
            "autocommit": "True",
        },
    )
    engine = sqlalchemy.create_engine(connection_url).execution_options(
        isolation_level="AUTOCOMMIT"
    )
    return engine


engine = get_engine()
engine.dialect.identifier_preparer.initial_quote = ""
engine.dialect.identifier_preparer.final_quote = ""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    """Get session method"""
    with Session(engine) as session:
        yield session
