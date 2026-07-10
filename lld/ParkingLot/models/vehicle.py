from abc import ABC
from dataclasses import dataclass
from models.enums import VehicleType


@dataclass
class Vehicle(ABC):
    registration_number: str
    vehicle_type: VehicleType


class MotorCycle(Vehicle):
    def __init__(self, registration_number: str) -> None:
        super().__init__(
            registration_number=registration_number,
            vehicle_type=VehicleType.MOTORCYCLE
        )


class Car(Vehicle):
    def __init__(self, registration_number: str) -> None:
        super().__init__(
            registration_number=registration_number,
            vehicle_type=VehicleType.CAR
        )


class Truck(Vehicle):
    def __init__(self,  registration_number: str) -> None:
        super().__init__(
            registration_number=registration_number,
            vehicle_type=VehicleType.TRUCK
        )
