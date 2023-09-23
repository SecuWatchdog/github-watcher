from pydantic import BaseModel

from app.models.organization_model import GitHubOrganization
from app.models.repository_model import GitHubRepository
from app.models.sender_model import GitHubSender


class RepoWebhookEvent(BaseModel):
    action: str
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubSender
