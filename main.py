import uvicorn
from fastapi import FastAPI
from app.handlers.webhook_router import router as webhook_router

app = FastAPI()

app.include_router(webhook_router, tags=["team events"])

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
