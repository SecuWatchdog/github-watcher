import logging
import os

import yaml

from app.notifiers.base.base_notification_service import BaseNotificationService


class LogNotifier(BaseNotificationService):
    def __init__(self, log_file_path):
        # Initialize notifications
        self.notifications = self.load_notifications(os.path.join(os.getcwd(), "app/notifiers", "notifications.yaml"))

        # Initialize logging
        self.logger = logging.getLogger('detector_logger')
        self.logger.setLevel(logging.INFO)

        # Create a file handler to write log results to a file
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)

        # Create a console handler to print log results to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Define the log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def load_notifications(self, yaml_file_path):
        with open(yaml_file_path, "r") as file:
            data = yaml.safe_load(file)
            return data.get("notifications", {})

    def get_notification_message(self, detector_name):
        return self.notifications.get(detector_name, {}).get("message", "No message found for detector.")

    def notify(self, detector):
        self.log_detection_result(detector, self.get_notification_message(detector))

    def log_detection_result(self, detector_name, msg):
        """
        Log a detection result.

        Args:
            detector_name (str): The name of the detector.
            msg (str): The result of the detection.
        """
        log_message = f"Detector '{detector_name}': {msg}"
        self.logger.info(log_message)
