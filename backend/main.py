"""Backend application entry point."""

from fastapi import FastAPI

app = FastAPI(
    title="SkillPrism AI"
)

@app.get("/")
def home():
    return {
        "message": "SkillPrism AI Backend Running"
    }
