from fastapi import APIRouter, HTTPException, Path, Request, BackgroundTasks
from app.db_config import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_root():
    return {"Hello": "World"}
