import json
from unittest import TestCase

from app.detectors.repo_detector import is_repository_live_time_is_valid
from app.models.repo_webhook_model import RepoWebhookEvent


class Test(TestCase):
    def test_hacker_repository_up_to_10_minutes(self):
        with(open("repo-sample-bad.json")) as data_file:
            repo_webhook_event = RepoWebhookEvent.model_validate(json.load(data_file))

        expected_result = True

        result = is_repository_live_time_is_valid(repo_webhook_event)

        self.assertEqual(result, expected_result)

    def test_legit_repository_lived_over_10_minutes(self):
        with(open("repo-sample.json")) as data_file:
            repo_webhook_event = RepoWebhookEvent.model_validate(json.load(data_file))
        expected_result = False

        result = is_repository_live_time_is_valid(repo_webhook_event)

        self.assertEqual(result, expected_result)
