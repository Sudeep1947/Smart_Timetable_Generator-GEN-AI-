
from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Smart Timetable Assistant AI")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Smart Timetable Assistant AI Running"}
