from models.parking_floor import ParkingFloor
from models.parking_spot import (
    CompactSpot,
    LargeSpot,
    MotorCycleSpot
)
from models.vehicle import Car, MotorCycle, Truck


def main() -> None:
    motorcycle_spot = MotorCycleSpot(
        spot_id="M1",
        floor_id="F1",
    )

    compact_spot = CompactSpot(
        spot_id="C1",
        floor_id="F1",
    )

    large_spot = LargeSpot(
        spot_id="L1",
        floor_id="F1",
    )

    floor = ParkingFloor(
        floor_id="F1",
        spots=[
            motorcycle_spot,
            compact_spot,
            large_spot,
        ],
    )

    print("Initially available spots:")
    for spot in floor.available_spots():
        print(spot.spot_id)

    print("\nAvailable count by spot type:")
    print(floor.available_count_by_spot_type())

    car = Car(
        registration_number="KL-01-AB-1234",
    )

    compact_spot.assign_vehicle(car)

    print("\nAfter parking a car:")
    print(floor.available_count_by_spot_type())

    print("\nFinding spot C1:")
    found_spot = floor.get_spot("C1")
    print(found_spot.spot_id)
    print(found_spot.is_available)

    compact_spot.remove_vehicle()

    print("\nAfter removing the car:")
    print(floor.available_count_by_spot_type())


if __name__ == "__main__":
    main()
