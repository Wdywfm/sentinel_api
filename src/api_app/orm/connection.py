from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api_app.settings import settings

engine = create_engine(
    f"postgresql://{settings.db_username}:{settings.db_username}@{settings.db_host}/{settings.db_name}"
)
session_maker = sessionmaker(bind=engine)


class Session:
    def __init__(self):
        self.session = session_maker()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
