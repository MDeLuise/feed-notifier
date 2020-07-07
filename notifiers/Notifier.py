from abc import ABC, abstractmethod


class Notifier(ABC):
    
    @abstractmethod
    def error(self, msg):
        pass

    @abstractmethod
    def notify(self, msg):
        pass