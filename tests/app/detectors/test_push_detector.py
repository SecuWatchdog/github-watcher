import json
from unittest import TestCase

from app.detectors.push_detector import is_bad_push_time
from app.models.push_webhook_model import PushWebhookEvent


class Test(TestCase):
    def test_legit_push_time(self):
        with(open("push-sample-legit.json")) as data_file:
            push_webhook_event = PushWebhookEvent.model_validate(json.load(data_file))

        result = is_bad_push_time(push_webhook_event)

        self.assertFalse(result)

    def test_bad_push_time(self):
        with(open("push-sample-bad.json")) as data_file:
            push_webhook_event = PushWebhookEvent.model_validate(json.load(data_file))

        result = is_bad_push_time(push_webhook_event)

        self.assertTrue(result)
