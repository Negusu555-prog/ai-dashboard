from fastapi import FastAPI
from routers import rag , agent  # ייבוא הrouters
from fastapi.middleware.cors import CORSMiddleware
import time 

# מונים בזיכרון
counters = {
    "rag_requests": 0,
    "agent_requests": 0,
    "error_count": 0,
    "latencies": []
}

app = FastAPI(
    title="AI Dashboard",
    description="Dashboard that displays RAG + Agents",
    version="1.0.0"
)

@app.middleware("http")
async def track_metrics(request, call_next):
    # שומרים זמן כניסה
    start_time = time.time()
    
    # מעבירים את הבקשה הלאה לendpoint
    response = await call_next(request)
    
    # חישוב כמה זמן לקח — בmilliseconds
    duration_ms = (time.time() - start_time) * 1000
    
    # סופרים לפי איזה שירות נקרא
    if "/rag" in request.url.path:
        counters["rag_requests"] += 1
    elif "/agent" in request.url.path:
        counters["agent_requests"] += 1
    
    # סופרים שגיאות — כל status code מ-400 ומעלה זו שגיאה
    if response.status_code >= 400:
        counters["error_count"] += 1
    
    # שומרים את הlatency — מגבילים ל-100 אחרונים
    counters["latencies"].append(duration_ms)
    if len(counters["latencies"]) > 100:
        counters["latencies"].pop(0)
    
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React מורשה
    allow_methods=["*"],
    allow_headers=["*"],
)


# רישום הrouters עם prefix
app.include_router(rag.router, prefix="/rag")
app.include_router(agent.router, prefix="/agent")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def get_metrics():
    # חישוב ממוצע latency — אם אין בקשות עדיין, מחזיר 0
    avg_latency = (
        sum(counters["latencies"]) / len(counters["latencies"])
        if counters["latencies"]
        else 0
    )
    
    return {
        "rag_requests": counters["rag_requests"],
        "agent_requests": counters["agent_requests"],
        "error_count": counters["error_count"],
        "avg_latency_ms": round(avg_latency, 2)
    }

