from fastapi import APIRouter, File, UploadFile, Form
import httpx

router = APIRouter()

RAG_SERVICE_URL = "http://rag-service:8001"  # כתובת ה-rag-service בתוך Docker



@router.post("/ask")
async def ask(file: UploadFile = File(...), question: str = Form(...)):
    async with httpx.AsyncClient() as client:
        # שלב 1 — העלאת הקובץ
        files = {"file": (file.filename, await file.read(), file.content_type)}
        await client.post(f"{RAG_SERVICE_URL}/upload", files=files, timeout=30.0)
        
        # שלב 2 — שאלה
        response = await client.post(
            f"{RAG_SERVICE_URL}/ask",
            json={"question": question},
            timeout=30.0
        )
    return response.json()
