from datetime import datetime


def calculate_time_difference(created_at: str, deleted_at: str) -> float:
    created_time = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    deleted_time = datetime.fromisoformat(deleted_at.replace("Z", "+00:00"))

    time_difference = (deleted_time - created_time).total_seconds() / 60.0

    return time_difference
