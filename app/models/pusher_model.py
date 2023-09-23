from pydantic import BaseModel, EmailStr


class GitHubPusher(BaseModel):
    name: str
    email: EmailStr
