
from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI(
    title="AI Research Agent",
    description="Agent that searches the web and reads URLs to answer research questions",
    version="1.0.0"
)

class ResearchRequest(BaseModel):
    task: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/research")
def research(request: ResearchRequest):
    result = run_agent(request.task)
    return {"result": result}