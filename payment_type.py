from enum import Enum
class PaymentType(Enum):
    CREDIT_CARD = "credit card"
    CASH = "cash"
    CHECK = "check"
    OTHER = "other"