from fastapi import APIRouter

from app.detectors.team_detector import detect_team
from app.models.repo_webhook_model import RepoWebhookEvent
from app.models.team_webhook_model import TeamWebhookEvent

router = APIRouter()


@router.post('/team')
async def handle_team_webhook(payload: TeamWebhookEvent):
    return detect_team(payload)


@router.post('/repo')
async def handle_team_webhook(payload: RepoWebhookEvent):
    return detect_team(payload)


@router.post('/push')
async def handle_team_webhook(payload: TeamWebhookEvent):
    return detect_team(payload)
