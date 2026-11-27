from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .db import connect, execute

app = FastAPI(
    title = "portfolio",
    version = "2.0"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactPayload(BaseModel):
    name: str
    mobile: str
    email: str
    reason: str
    comment: str

@app.post("/api/contact")
def submit_data(payload : ContactPayload):
    try:
        with connect() as conn:
            new_id = execute(
                conn, 
                """
                INSERT INTO contacts (name, mobile, email, reason, comment)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    payload.name,
                    payload.mobile,
                    payload.email,
                    payload.reason,
                    payload.comment,
                ),
            )
            conn.commit()
            return {"status": "success", "id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))