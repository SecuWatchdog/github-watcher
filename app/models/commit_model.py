from typing import List

from pydantic import BaseModel, HttpUrl

from app.models.author_model import GitHubCommitAuthor


class GitHubCommit(BaseModel):
    id: str
    tree_id: str
    distinct: bool
    message: str
    timestamp: str
    url: HttpUrl
    author: GitHubCommitAuthor
    committer: GitHubCommitAuthor
    added: List[str]
    removed: List[str]
    modified: List[str]
