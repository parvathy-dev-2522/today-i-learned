from enum import Enum, auto


class VehicleType(Enum):
    MOTORCYCLE = auto()
    CAR = auto()
    TRUCK = auto()


class SpotType(Enum):
    MOTORCYCLE = auto()
    COMPACT = auto()
    LARGE = auto()


class SpotStatus(Enum):
    AVAILABLE = auto()
    OCCUPIED = auto()


class TicketStatus(Enum):
    ACTIVE = auto()
    PAID = auto()
    LOST = auto()
    CANCELLED = auto()


class PaymentStatus(Enum):
    PENDING = auto()
    SUCCESS = auto()
    FAILED = auto()
