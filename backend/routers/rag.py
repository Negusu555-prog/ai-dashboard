from fastapi import APIRouter, File, UploadFile, Form
import httpx

router = APIRouter()

RAG_SERVICE_URL = "http://rag-service:8001"  # כתובת ה-rag-service בתוך Docker



@router.post("/ask")
async def ask(file: UploadFile = File(...), question: str = Form(...)):
    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, await file.read(), file.content_type)}
        data = {"question": question}
        response = await client.post(
            f"{RAG_SERVICE_URL}/ask",
            files=files,
            data=data,
            timeout=30.0
        )
    return response.json()

