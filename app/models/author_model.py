from pydantic import BaseModel, EmailStr


class GitHubCommitAuthor(BaseModel):
    name: str
    email: EmailStr
    username: str
