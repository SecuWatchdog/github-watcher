from typing import List, Optional, Union

from pydantic import HttpUrl, BaseModel

from app.models.owner_model import GitHubOwner


class GitHubRepository(BaseModel):
    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: GitHubOwner
    html_url: HttpUrl
    description: Optional[str] = None
    fork: bool
    url: HttpUrl
    forks_url: HttpUrl
    keys_url: HttpUrl
    collaborators_url: HttpUrl
    teams_url: HttpUrl
    hooks_url: HttpUrl
    issue_events_url: HttpUrl
    events_url: HttpUrl
    assignees_url: HttpUrl
    branches_url: HttpUrl
    tags_url: HttpUrl
    blobs_url: HttpUrl
    git_tags_url: HttpUrl
    git_refs_url: HttpUrl
    trees_url: HttpUrl
    statuses_url: HttpUrl
    languages_url: HttpUrl
    stargazers_url: HttpUrl
    contributors_url: HttpUrl
    subscribers_url: HttpUrl
    subscription_url: HttpUrl
    commits_url: HttpUrl
    git_commits_url: HttpUrl
    comments_url: HttpUrl
    issue_comment_url: HttpUrl
    contents_url: HttpUrl
    compare_url: HttpUrl
    merges_url: HttpUrl
    archive_url: HttpUrl
    downloads_url: HttpUrl
    issues_url: HttpUrl
    pulls_url: HttpUrl
    milestones_url: HttpUrl
    notifications_url: HttpUrl
    labels_url: HttpUrl
    releases_url: HttpUrl
    deployments_url: HttpUrl
    created_at: Optional[Union[int, str]]
    updated_at: str
    pushed_at: Optional[Union[int, str]]
    git_url: str
    ssh_url: str
    clone_url: HttpUrl
    svn_url: HttpUrl
    homepage: Optional[HttpUrl] = None
    size: int
    stargazers_count: int
    watchers_count: int
    language: Optional[str] = None
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    has_discussions: bool
    forks_count: int
    mirror_url: Optional[HttpUrl] = None
    archived: bool
    disabled: bool
    open_issues_count: int
    license: Optional[str] = None
    allow_forking: bool
    is_template: bool
    web_commit_signoff_required: bool
    topics: List[str] = []
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str
    stargazers: Optional[int] = None
    master_branch: Optional[str] = None
