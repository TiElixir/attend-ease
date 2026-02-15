from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

# Load schedule data once
# Assuming data is in ../data/schedule.json (relative to backend/)
SCHEDULE_PATH = os.path.join(os.path.dirname(__file__), "../data/schedule.json")

@router.get("/")
def get_schedule():
    try:
        if not os.path.exists(SCHEDULE_PATH):
             raise HTTPException(status_code=404, detail="Schedule file not found")
             
        with open(SCHEDULE_PATH, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        if isinstance(e, HTTPException): raise e
        raise HTTPException(status_code=500, detail=str(e))
