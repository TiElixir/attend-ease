import firebase_admin
from firebase_admin import credentials, firestore, auth

firebase_auth = auth
import os
from dotenv import load_dotenv

load_dotenv()


try:
    # Check if app is already initialized to avoid errors during hot reload
    app = firebase_admin.get_app()
except ValueError:
    # Vercel: Load from ENV variable string
    firebase_sa_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")
    
    if firebase_sa_json:
        import json
        cred_dict = json.loads(firebase_sa_json)
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
    
    # Local: Load from file if exists
    elif os.path.exists("backend/serviceAccountKey.json"):
        cred = credentials.Certificate("backend/serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        
    # Fallback to default (Google Cloud Run / Local with Auth set)
    else:
        firebase_admin.initialize_app()

db = firestore.client()

def get_db():
    return db
