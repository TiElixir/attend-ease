from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import students, schedule, auth
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AttendEase Backend")

# Allow CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:9002",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:9002"
    ], # Adjust ports as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])
from routers import admin
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def read_root():
    return {"message": "AttendEase API is running"}
