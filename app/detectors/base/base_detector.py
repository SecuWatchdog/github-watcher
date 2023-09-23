from abc import abstractmethod


class BaseDetector:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def detect(self, event):
        raise NotImplementedError("Subclasses must implement the detect method")
