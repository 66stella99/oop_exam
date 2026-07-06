from abc import ABC, abstractmethod
from cutomer import Customer
from payment_type import PaymentType
from datetime import datetime
class Order(ABC):
    existing_ids = []

    def __init__(self, order_id, name, delivery_address, items,
                 customer: Customer, payment_type: PaymentType):
        if order_id in Order.existing_ids:
            raise ValueError(f"Order id '{order_id}' already exists.")
        Order.existing_ids.append(order_id)

        self.id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = datetime.now()

        self.total_price = self.calculate_total_price()

        # add all order items to the customer's favorites
        customer.add_order_items_to_favorites(items)

    def sum_items(self):
        total = 0
        for item in self.items:
            total += item.item_price
        return total

    @abstractmethod
    def calculate_total_price(self):
        pass