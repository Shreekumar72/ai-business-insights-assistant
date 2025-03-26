from fastapi import FastAPI
from pydantic import BaseModel
from ai_query_engine import get_business_insight

app = FastAPI()

# ✅ New: Welcome route to fix 404 on "/"
@app.get("/")
def root():
    return {"message": "Welcome to the AI Business Insights API! Visit /docs to test."}

# Request model
class QueryRequest(BaseModel):
    question: str

# Main AI route
@app.post("/generate-insight")
def generate_insight(request: QueryRequest):
    result = get_business_insight(request.question)
    return {"insight": result}
