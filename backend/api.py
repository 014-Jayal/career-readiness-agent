# backend/api.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.graph.agent_graph import build_graph

# -------------------------
# App Initialization
# -------------------------
app = FastAPI(title="AI Career Readiness Agent")

# Enable CORS (for Streamlit / Swagger / Browser access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # demo-friendly
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Build LangGraph once at startup
graph = build_graph()

# -------------------------
# Request Schema
# -------------------------
class CareerRequest(BaseModel):
    resume_text: str
    target_role: str


# -------------------------
# API Endpoint
# -------------------------
@app.post("/analyze-career")
def analyze_career(data: CareerRequest):
    try:
        result = graph.invoke({
            "resume_text": data.resume_text,
            "target_role": data.target_role
        })

        return {
            "readiness_score": result["readiness_score"],
            "existing_skills": result["skill_gap"]["matched_skills"],
            "missing_skills": result["skill_gap"]["missing_skills"],
            "learning_roadmap": result["learning_roadmap"]
        }

    except KeyError:
        return {
            "error": "Invalid target_role. Please choose a supported job role."
        }
