from app.detectors.base.base_detector import BaseDetector
from app.models.team_webhook_model import TeamWebhookEvent


class TeamDetector(BaseDetector):
    def detect(self, event):
        return self.is_hacker_team(event)

    def is_hacker_team(self, payload: TeamWebhookEvent):
        if payload.action == 'created':
            team_name = payload.team.name
            if team_name.startswith('hacker'):
                return True

        return True
