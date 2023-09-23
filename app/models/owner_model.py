from typing import Optional

from pydantic import BaseModel, HttpUrl, EmailStr


class GitHubOwner(BaseModel):
    name: Optional[str] = ""
    email: Optional[EmailStr] = None
    login: str
    id: int
    node_id: str
    avatar_url: HttpUrl
    gravatar_id: Optional[str] = ""
    url: HttpUrl
    html_url: str
    followers_url: HttpUrl
    following_url: HttpUrl
    gists_url: HttpUrl
    starred_url: HttpUrl
    subscriptions_url: HttpUrl
    organizations_url: HttpUrl
    repos_url: HttpUrl
    events_url: HttpUrl
    received_events_url: HttpUrl
    type: str
    site_admin: bool
