from fastapi import FastAPI

from api_app.orm import connection, models
from api_app.router import router

models.Base.metadata.create_all(bind=connection.engine)

app = FastAPI()

app.include_router(router)
