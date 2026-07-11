from models.parking_spot import ParkingSpot
from collections import Counter


class ParkingFloor:
    """Represents one floor of the parking lot."""

    def __init__(self, floor_id: str, spots: list[ParkingSpot]):
        # Unique identifier of the parking floor.
        self.floor_id = floor_id
        # List of all parking spots available on this floor.
        self.spots = spots

    def available_spots(self) -> list[ParkingSpot]:
        """Return all currently available parking spots on the floor."""
        # Include only spots that do not have a vehicle assigned.

        available_spots = []
        for spot in self.spots:
            if spot.is_available:
                available_spots.append(spot)
        return available_spots

        # (or use List comprehension)
        # return [
        #     spot
        #     for spot in self.spots
        #     if spot.is_available
        # ]

    def available_count_by_spot_type(self) -> dict[str, int]:
        """Return the number of available spots grouped by spot type."""
        # Count available spots such as MOTORCYCLE, COMPACT, and LARGE
        counts = Counter(
            spot.spot_type.name
            for spot in self.available_spots()
        )
        # Convert Counter into a normal dictionary.
        return dict(counts)

    def get_spot(self, spot_id: str) -> ParkingSpot:
        """Find and return a parking spot using its ID."""

        # Search through all spots on this floor.
        for spot in self.spots:
            if spot.spot_id == spot_id:
                return spot

        # Raise an error when the requested spot does not exist.
        raise ValueError(
            f"Spot {spot_id} was not found on floor {self.floor_id}."
        )
