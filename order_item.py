class OrderItem:
    existing_ids = []

    def __init__(self, item_id, item_name, item_price):
        OrderItem.existing_ids.append(item_id)

        self.id = item_id
        self.item_name = item_name
        self.item_price = item_price
