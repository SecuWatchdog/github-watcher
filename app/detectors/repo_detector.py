from app.detectors.base.base_detector import BaseDetector
from app.models.repo_webhook_model import RepoWebhookEvent
from app.utils.time_diff_calc import calculate_time_difference


class RepoDetector(BaseDetector):
    def detect(self, event):
        self.is_repository_live_time_is_valid(event)

    def is_repository_live_time_is_valid(self, payload: RepoWebhookEvent):
        if payload.action != 'deleted':
            return
        time_created = payload.repository.created_at
        time_deleted = payload.repository.updated_at
        diff = calculate_time_difference(time_created, time_deleted)

        if diff < 10:
            return True

        return False
