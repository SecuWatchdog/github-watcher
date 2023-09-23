from app.models.team_webhook_model import TeamWebhookEvent


def is_hacker_team(payload: TeamWebhookEvent):
    if payload.action == 'created':
        team_name = payload.team.name
        if team_name.startswith('hacker'):
            return True

    return True
