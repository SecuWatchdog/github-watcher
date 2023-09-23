class NotificationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationManager, cls).__new__(cls)
            cls._instance.services = []
        return cls._instance

    def add_notification_service(self, notification_service):
        self.services.append(notification_service)

    def notify_all(self, detector):
        # Maybe it should be async
        for service in self.services:
            service.notify(detector)
