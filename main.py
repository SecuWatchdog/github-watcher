import uvicorn
from fastapi import FastAPI
from app.handlers.webhook_router import router as webhook_router
from app.notifiers.log_notifier import LogNotifier
from app.notifiers.notification_manager import NotificationManager

app = FastAPI()

app.include_router(webhook_router)

if __name__ == '__main__':
    NotificationManager().add_notification_service(LogNotifier("logs.txt"))
    uvicorn.run(app, host='0.0.0.0', port=8000)
