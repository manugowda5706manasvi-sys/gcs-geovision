from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///./campus_security.db"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session