from abc import ABC, abstractmethod
class CustomerGift(ABC):

    @abstractmethod
    def open_gift(self):
        pass


class GenericGift(CustomerGift):
    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")
