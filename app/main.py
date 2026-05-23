from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db

app = FastAPI()


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        return {
            "status": "success",
            "result": result[0]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }