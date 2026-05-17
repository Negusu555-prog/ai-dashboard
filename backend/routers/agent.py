from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter()

AGENT_SERVICE_URL = "http://agent-service:8002"  # כתובת ה-agent-service בתוך Docker

class ResearchRequest(BaseModel):
    task: str

@router.post("/research")
async def research(request: ResearchRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{AGENT_SERVICE_URL}/research",
            json={"task": request.task},
            timeout=30.0  # מחכה עד 30 שניות לתשובה
        )
    return response.json()