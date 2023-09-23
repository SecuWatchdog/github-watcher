from fastapi import APIRouter, Depends

from app.detectors.push_detector import is_bad_push_time
from app.detectors.repo_detector import is_repository_live_time_is_valid
from app.detectors.team_detector import is_hacker_team
from app.models.push_webhook_model import PushWebhookEvent
from app.models.repo_webhook_model import RepoWebhookEvent
from app.models.team_webhook_model import TeamWebhookEvent
from app.notifiers.notification_manager import NotificationManager

router = APIRouter()
notification_manager = NotificationManager()


@router.post('/team')
async def handle_team_webhook(payload: TeamWebhookEvent, notification_manager: NotificationManager = Depends()):
    if is_hacker_team(payload):
        notification_manager.notify_all("team-hack")
    return 202


@router.post('/repo')
async def handle_repo_webhook(payload: RepoWebhookEvent, notification_manager: NotificationManager = Depends()):
    if is_repository_live_time_is_valid(payload):
        notification_manager.notify_all("repo-deleted")
    return 202


@router.post('/push')
async def handle_push_webhook(payload: PushWebhookEvent, notification_manager: NotificationManager = Depends()):
    if is_bad_push_time(payload):
        notification_manager.notify_all("push-bad-time")
    return 202
