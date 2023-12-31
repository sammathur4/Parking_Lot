from backend.parking_lot import *
import pytest


class TestParkingLot:

    #  Assign parking spot to a vehicle with a valid vehicle number
    def test_assign_parking_spot_valid_vehicle_number(self):
        parking_lot = ParkingLot()
        result = parking_lot.assign_parking_spot("ABC123")
        assert result == {"level": 1, "spot": 1}

    #  Retrieve parking spot of a vehicle that was previously parked
    def test_retrieve_parking_spot_previously_parked_vehicle(self):
        parking_lot = ParkingLot()
        parking_lot.assign_parking_spot("ABC123")
        result = parking_lot.retrieve_parking_spot("ABC123")
        assert result == {"level": 1, "spot": 1}

    #  Assign parking spot to multiple vehicles with valid vehicle numbers
    def test_assign_parking_spot_multiple_valid_vehicle_numbers(self):
        parking_lot = ParkingLot()
        result1 = parking_lot.assign_parking_spot("ABC123")
        result2 = parking_lot.assign_parking_spot("DEF456")
        assert result1 == {"level": 1, "spot": 1}
        assert result2 == {"level": 1, "spot": 2}

    #  Assign parking spot to a vehicle with an empty vehicle number
    def test_assign_parking_spot_empty_vehicle_number(self):
        parking_lot = ParkingLot()
        result = parking_lot.assign_parking_spot("")
        assert result == {"message": "Invalid vehicle number"}

    #  Assign parking spot to a vehicle with a None vehicle number
    def test_assign_parking_spot_none_vehicle_number(self):
        parking_lot = ParkingLot()
        result = parking_lot.assign_parking_spot(None)
        assert result == {"message": "Invalid vehicle number"}

    #  Assign parking spot to a vehicle with a vehicle number that is already parked in the parking lot
    def test_assign_parking_spot_already_parked_vehicle_number(self):
        parking_lot = ParkingLot()
        parking_lot.assign_parking_spot("ABC123")
        result = parking_lot.assign_parking_spot("ABC123")
        assert result == {"level": 1, "spot": 1}

    #  Retrieve parking spot of multiple vehicles that were previously parked
    def test_retrieve_parking_spot_multiple_vehicles(self):
        parking_lot = ParkingLot()
        parking_lot.assign_parking_spot("ABC123")
        parking_lot.assign_parking_spot("DEF456")
        result1 = parking_lot.retrieve_parking_spot("ABC123")
        result2 = parking_lot.retrieve_parking_spot("DEF456")
        assert result1 == {"level": 1, "spot": 1}
        assert result2 == {"level": 1, "spot": 2}

    def test_assign_parking_spot_parking_lot_full(self):
        parking_lot = ParkingLot(num_levels=1, spots_per_level=1)
        parking_lot.assign_parking_spot("ABC123")
        result = parking_lot.assign_parking_spot("XYZ789")
        assert result == {"message": "Parking lot is full"}
