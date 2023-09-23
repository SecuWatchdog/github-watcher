from typing import Union

from fastapi import APIRouter, Depends, Header
from starlette.responses import JSONResponse

from app.detectors.push_detector import PushDetector
from app.detectors.repo_detector import RepoDetector
from app.detectors.team_detector import TeamDetector
from app.models.push_webhook_model import PushWebhookEvent
from app.models.repo_webhook_model import RepoWebhookEvent
from app.models.team_webhook_model import TeamWebhookEvent
from app.notifiers.notification_manager import NotificationManager

router = APIRouter()
notification_manager = NotificationManager()

detectors = {
    'team': (TeamDetector("team-hack"),),
    'repository': (RepoDetector("repo-deleted"),),
    'push': (PushDetector("push-bad-time"),),
}


@router.post("/webhook")
async def handle_webhook(payload: Union[TeamWebhookEvent, RepoWebhookEvent, PushWebhookEvent],
                         x_github_event: str = Header(None),
                         notification_manager: NotificationManager = Depends()):
    selected_detectors = detectors.get(x_github_event, ())

    for detector in selected_detectors:
        if detector.detect(payload):
            notification_manager.notify_all(detector.name)

    return JSONResponse(content={}, status_code=202)
