from datetime import datetime

from app.models.push_webhook_model import PushWebhookEvent


def is_bad_push_time(event: PushWebhookEvent):
    unix_timestamp = event.repository.pushed_at
    commit_time = datetime.utcfromtimestamp(unix_timestamp)

    start_time = commit_time.replace(hour=14, minute=0, second=0)
    end_time = commit_time.replace(hour=16, minute=0, second=0)

    if start_time <= commit_time <= end_time:
        return True
    else:
        return False
