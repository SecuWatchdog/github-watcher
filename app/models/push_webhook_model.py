from typing import List, Optional

from pydantic import BaseModel, HttpUrl

from app.models.commit_model import GitHubCommit
from app.models.organization_model import GitHubOrganization
from app.models.pusher_model import GitHubPusher
from app.models.repository_model import GitHubRepository
from app.models.sender_model import GitHubSender


class PushWebhookEvent(BaseModel):
    ref: str
    before: str
    after: str
    repository: GitHubRepository
    pusher: GitHubPusher
    organization: GitHubOrganization
    sender: GitHubSender
    created: bool
    deleted: bool
    forced: bool
    base_ref: Optional[str] = None
    compare: HttpUrl
    commits: List[GitHubCommit]
    head_commit: GitHubCommit
