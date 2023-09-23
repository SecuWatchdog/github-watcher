from pydantic import BaseModel

from app.models.organization_model import GitHubOrganization
from app.models.sender_model import GitHubSender
from app.models.team_model import GitHubTeam


class TeamWebhookEvent(BaseModel):
    action: str
    team: GitHubTeam
    organization: GitHubOrganization
    sender: GitHubSender
