from fastapi import FastAPI
from routers import rag , agent  # ייבוא הrouters

app = FastAPI(
    title="AI Dashboard",
    description="Dashboard that displays RAG + Agents",
    version="1.0.0"
)

# רישום הrouters עם prefix
app.include_router(rag.router, prefix="/rag")
app.include_router(agent.router, prefix="/agent")

@app.get("/health")
def health():
    return {"status": "ok"}