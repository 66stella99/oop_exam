from abc import ABC, abstractmethod
class CustomerType(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def is_vip(self):
        pass
