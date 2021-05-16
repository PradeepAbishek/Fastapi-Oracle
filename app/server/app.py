from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from .api.api import router as api_router
from .db.config import PROJECT_NAME
from .db.connection import get_db, engine
from .db import tables

# tables.Base.metadata.create_all(bind=engine) # Creates a table

app = FastAPI(title=PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", get_db)

app.include_router(api_router)
