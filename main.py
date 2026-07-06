from order_item import OrderItem
from vip_order import VIPOrder
from payment_type import PaymentType
from cutomer import Customer
from vip import Vip
from regular import Regular
from regular_order import RegularOrder
from generic_gift import GenericGift

if __name__ == "__main__":
    print("Order Management System Demo")
    print("-" * 50)

    item1 = OrderItem("1", "Laptop", 1000)
    item2 = OrderItem("2", "Mouse", 50)
    item3 = OrderItem("3", "Keyboard", 80)

    regular_customer = Customer("C1", "stella", "chulak", "stella@gmail.com",
                                "levontin", Regular())

    vip_customer = Customer("C2", "ben", "meir", "ben@gmail.com",
                            "shaul hamelec", Vip(),
                            customer_discount=10)

    order1 = RegularOrder("1", "Order", "levontin",
                          [item1, item2], regular_customer,
                          PaymentType.CREDIT_CARD)
    print("stella's", order1.total_price)
    print("stella's favorites:", [i.item_name for i in regular_customer.favorite_items])

    order2 = VIPOrder("O2", "ben's VIP Order", "shaul hamelec",
                      [item3], vip_customer, PaymentType.CASH)
    print("Order2 total price with discount:", order2.total_price)

    try:
        item4 = OrderItem("I4", "Monitor", 200)
        VIPOrder("O3", "Invalid VIP order", "123 Main St",
                 [item4], regular_customer, PaymentType.OTHER)
    except ValueError as e:
        print("Caught expected error:", e)

    gift = GenericGift()
    vip_customer.take_gift(gift)
    vip_customer.open_gift()