from abc import abstractmethod


class BaseNotificationService:
    @abstractmethod
    def notify(self, detector):
        pass
