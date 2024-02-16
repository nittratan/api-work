from fastapi import FastAPI
from api.router import api_router
from db.connection import connect_to_mongodb, close_mongodb_connection

app = FastAPI()

app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    connect_to_mongodb()
    print("Application has started")

@app.on_event("shutdown")
async def shutdown_event():
    close_mongodb_connection()
    print("Application shutting down")
