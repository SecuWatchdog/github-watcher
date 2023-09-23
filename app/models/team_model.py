from typing import Optional

from pydantic import BaseModel


class GitHubTeam(BaseModel):
    name: str
    id: int
    node_id: str
    slug: str
    description: str
    privacy: str
    notification_setting: str
    url: str
    html_url: str
    members_url: str
    repositories_url: str
    permission: str
    parent: Optional[str] = None
