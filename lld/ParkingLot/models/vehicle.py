from abc import ABC
from dataclasses import dataclass
from models.enums import VehicleType


@dataclass
class Vehicle(ABC):  # Base class for all vehicle types.
    registration_number: str
    vehicle_type: VehicleType


class MotorCycle(Vehicle):  # Initialize a motorcycle with its vehicle type.
    def __init__(self, registration_number: str) -> None:
        super().__init__(
            registration_number=registration_number,
            vehicle_type=VehicleType.MOTORCYCLE
        )


class Car(Vehicle):  # Initialize a car with its vehicle type.
    def __init__(self, registration_number: str) -> None:
        super().__init__(
            registration_number=registration_number,
            vehicle_type=VehicleType.CAR
        )


class Truck(Vehicle):  # Initialize a truck with its vehicle type.
    def __init__(self,  registration_number: str) -> None:
        super().__init__(
            registration_number=registration_number,
            vehicle_type=VehicleType.TRUCK
        )
