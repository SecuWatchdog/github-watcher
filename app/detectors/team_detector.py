from app.models.team_webhook_model import TeamWebhookEvent


def detect_team(payload: TeamWebhookEvent):
    if payload.action == 'created':
        team_name = payload.team.name
        if team_name.startswith('hacker'):
            return {'message': 'Team creation with prefix "hacker" detected.'}

    return {'message': 'Team event handled successfully'}
