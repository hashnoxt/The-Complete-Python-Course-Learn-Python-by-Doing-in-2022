from database import Database
from abc import ABCMeta, abstractmethod

class Savable(mataclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass