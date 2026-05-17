from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter()

RAG_SERVICE_URL = "http://rag-service:8001"  # כתובת ה-rag-service בתוך Docker

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask(request: AskRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{RAG_SERVICE_URL}/ask",
            json={"question": request.question},
            timeout=30.0  # מחכה עד 30 שניות לתשובה
        )
    return response.json()

