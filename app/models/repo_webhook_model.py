from pydantic import BaseModel

from app.models.owner_model import GitHubOwner
from app.models.repository_model import GitHubRepository
from app.models.sender_model import GitHubSender


class RepoWebhookEvent(BaseModel):
    action: str
    repository: GitHubRepository
    organization: GitHubOwner
    sender: GitHubSender
