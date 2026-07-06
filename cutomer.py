from customer_type import CustomerType
class Customer:
    existing_ids = []

    def __init__(self, customer_id, first_name, last_name, email,
                 delivery_address, customer_type: CustomerType,
                 customer_discount=None):
        if customer_id in Customer.existing_ids:
            raise ValueError(f"Customer {customer_id} already exists.")
        Customer.existing_ids.append(customer_id)

        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = []
        self.customer_gift = None

    def add_order_items_to_favorites(self, items):
        for item in items:
            already_in_favorites = False
            for favorite in self.favorite_items:
                if favorite.item_name == item.item_name:
                    already_in_favorites = True
                    break
            if not already_in_favorites:
                self.favorite_items.append(item)

    def add_favorite_item(self, item):
        self.favorite_items.append(item)

    def remove_favorite_item(self, item):
        self.favorite_items.remove(item)

    def take_gift(self, gift):
        self.customer_gift = gift

    def open_gift(self):
        if self.customer_gift is None:
            print(f"{self.first_name} has no gift.")
        else:
            self.customer_gift.open_gift()
