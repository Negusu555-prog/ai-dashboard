from fastapi import APIRouter 
from pydantic import BaseModel

router = APIRouter(prefix="/rag")

class ASK(BaseModel):
   question: str