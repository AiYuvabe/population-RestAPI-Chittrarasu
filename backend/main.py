from fastapi import FastAPI
from backend.routes.continents import router
from backend.logger import logger
from backend.routes.continents import router

app = FastAPI()

# Include API routes
app.include_router(router)

logger.info("Starting FastAPI application...")

@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to the World Population API"}
