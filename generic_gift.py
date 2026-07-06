from cutomer_gift import CustomerGift
from overrides import overrides
class GenericGift(CustomerGift):
    @overrides
    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")

