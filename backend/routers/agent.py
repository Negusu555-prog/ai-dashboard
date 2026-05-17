from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()  

class ResearchRequest(BaseModel):
    task: str

@router.post("/research")
def research(request: ResearchRequest):
    return {"status": "ok", "task": request.task}