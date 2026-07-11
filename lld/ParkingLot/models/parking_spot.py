from abc import ABC, abstractmethod
from models.enums import SpotType, VehicleType
from models.vehicle import Vehicle


"""
Assumption (Parking Rule):
# Motorcycle Spot -> Motorcycle only
# Compact Spot    -> Motorcycle + Car
# Large Spot      -> Motorcycle + Car + Truck
# Rule of Thumb:
# Bigger spots can accommodate smaller vehicles,
# but smaller spots cannot accommodate larger vehicles.
"""


class ParkingSpot(ABC):  # Initialize the parking spot with its details.
    def __init__(self, spot_id: str, floor_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.floor_id = floor_id
        self.spot_type = spot_type
        # Empty spot.  No vehicle is assigned when the spot is created.
        self.vehicle = None
        # self.vehicle: Optional[Vehicle] = None ## (Another Syntax)It means the variable can hold either:a Vehicle object, or None.
        # Optional[Vehicle] is equivalent to Vehicle|None

    @property
    # Check whether the parking spot is available.
    def is_available(self) -> bool:
        # if self.vehicle is None:
        #     return True
        # else:
        #     return False
        return self.vehicle is None

    @abstractmethod
    # Ensure every parking spot defines its own fitting logic, later.
    def can_fit(self, vehicle: Vehicle) -> bool:
        pass

    # Assign a vehicle to the parking spot.
    def assign_vehicle(self, vehicle: Vehicle) -> None:
        if not self.is_available:  # Prevent parking if the spot is already occupied.
            raise ValueError(f"Spot {self.spot_id} is already occupied")

        # Ensure the vehicle is compatible with the spot type.
        if not self.can_fit(vehicle):
            raise ValueError(
                f"{vehicle.vehicle_type.name} cannot fit in {self.spot_type.name}")

        self.vehicle = vehicle  # Mark the parking spot as occupied.

    # Remove the vehicle from the parking spot.
    def remove_vehicle(self):
        # Prevent removing a vehicle from an empty spot.
        if (self.vehicle is None):
            raise ValueError(f"Spot {self.spot_id} is already empty")
        removed_vehicle = self.vehicle
        self.vehicle = None  # Mark the parking spot as available again.
        return removed_vehicle  # Return the removed vehicle.


class MotorCycleSpot(ParkingSpot):
    # Initialize a motorcycle parking spot.
    # Allow only motorcycles.
    def __init__(self, spot_id: str, floor_id: str) -> None:
        super().__init__(
            spot_id=spot_id,
            floor_id=floor_id,
            spot_type=SpotType.MOTORCYCLE
        )

    def can_fit(self, vehicle) -> bool:
        # if (vehicle.vehicle_type == VehicleType.MOTORCYCLE):
        #     return True
        # else:
        #     return False
        return vehicle.vehicle_type == VehicleType.MOTORCYCLE


class CompactSpot(ParkingSpot):
    # Initialize a compact parking spot.
    # Allow motorcycles and cars only.
    def __init__(self, spot_id: str, floor_id: str) -> None:
        super().__init__(
            spot_id=spot_id,
            floor_id=floor_id,
            spot_type=SpotType.COMPACT
        )

    def can_fit(self, vehicle) -> bool:
        return vehicle.vehicle_type in {
            vehicle.vehicle_type == VehicleType.CAR,
            vehicle.vehicle_type == VehicleType.MOTORCYCLE
        }


class LargeSpot(ParkingSpot):
    # Initialize a large parking spot.
    # Allow all vehicle types.
    def __init__(self, spot_id: str, floor_id: str) -> None:
        super().__init__(
            spot_id=spot_id,
            floor_id=floor_id,
            spot_type=SpotType.MOTORCYCLE
        )

    def can_fit(self, vehicle) -> bool:
        # if (vehicle.vehicle_type == VehicleType.MOTORCYCLE):
        #     return True
        # else:
        #     return False
        return vehicle.vehicle_type == VehicleType.MOTORCYCLE
